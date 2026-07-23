# 04_youtube_search_and_validate.py
current_year = datetime.now().year
search_queries = [f"капсульный гардероб обзор брендов {current_year}", "базовый гардероб минимализм стиль", "мода локальные бренды одежды"]

MIN_SUBS, MAX_SUBS, MAX_AGE_DAYS = 3000, 500000, 90
found_channels = []

for query in search_queries:
    try:
        search_resp = youtube.search().list(q=query, part='snippet', type='channel', maxResults=5, relevanceLanguage='ru').execute()
        for item in search_resp.get('items', []):
            ch_id = item['snippet']['channelId']
            ch_resp = youtube.channels().list(part='statistics,snippet', id=ch_id).execute()
            if ch_resp.get('items'):
                ch_data = ch_resp['items'][0]
                subs = int(ch_data['statistics'].get('subscriberCount', 0))
                if MIN_SUBS <= subs <= MAX_SUBS:
                    vid_resp = youtube.search().list(channelId=ch_id, part='snippet', order='date', maxResults=1).execute()
                    if vid_resp.get('items'):
                        last_vid = vid_resp['items'][0]
                        pub_date = datetime.strptime(last_vid['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
                        days_ago = (datetime.now(timezone.utc) - pub_date).days
                        if days_ago <= MAX_AGE_DAYS:
                            found_channels.append({'name': ch_data['snippet']['title'], 'url': f"https://www.youtube.com/channel/{ch_id}", 'subscribers': subs, 'description': ch_data['snippet'].get('description', ''), 'last_video_title': last_vid['snippet']['title'], 'last_video_date': pub_date.strftime('%Y-%m-%d'), 'days_since_last_video': days_ago})
                            if len(found_channels) >= 3: break
    except Exception: pass

with open(f"{ARTIFACTS_DIR}/found_youtube_channels.json", 'w', encoding='utf-8') as f:
    json.dump(found_channels, f, ensure_ascii=False, indent=2)
