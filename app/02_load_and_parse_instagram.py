# 02_load_and_parse_instagram.py
import re
from instagrapi import Client
from instagrapi.exceptions import UserNotFound, PrivateAccount

# Загрузка Excel (умный поиск столбца с URL)
FILE_PATH = f"{BASE_DIR}/blogers.xlsx"
df_raw = pd.read_excel(FILE_PATH, header=None)
url_col_idx = None
for col_idx in range(len(df_raw.columns)):
    sample = df_raw.iloc[:5, col_idx].astype(str)
    if sum(1 for val in sample if 'instagram.com' in val) >= 2:
        url_col_idx = col_idx
        break

df_input = df_raw.iloc[:, [url_col_idx]].copy() if url_col_idx is not None else pd.DataFrame()
df_input.columns = ['url']
df_input = df_input.dropna().reset_index(drop=True)
df_input['url'] = df_input['url'].astype(str).str.strip()

# Парсер с Circuit Breaker (Fallback на моки при блокировке)
cl = Client()
# cl.login_by_sessionid("ВАШ_SESSION_ID") # Раскомментировать при наличии session.txt

def get_blogger_data(url: str) -> dict:
    match = re.search(r'instagram\.com/([a-zA-Z0-9_.]+)', url.split('?')[0])
    if not match: return None
    username = match.group(1).rstrip('/')
    try:
        user = cl.user_info_by_username(username)
        posts = []
        for i, media in enumerate(cl.user_medias(user.pk, amount=3)):
            if i >= 3: break
            posts.append(media.caption_text[:150] if media.caption_text else "Без описания")
        return {"username": username, "bio": user.biography or "Нет био", "followers": user.follower_count, "recent_posts": posts, "source": "real"}
    except (UserNotFound, PrivateAccount, Exception):
        return {"username": username, "bio": "Fashion & Lifestyle blogger", "followers": 45000, "recent_posts": ["Капсульный гардероб", "Обзор тканей"], "source": "mock_fallback"}

profiles_data = [get_blogger_data(row['url']) for _, row in df_input.iterrows() if get_blogger_data(row['url'])]
