# 05_generate_pasta_offers_and_save.py
offers_results = []
brand_info = "LD LATTE — бренд женской одежды. Создаём с нуля: от эскиза до готового товара на Wildberries и Ozon. С 2022 года выросли с нуля до оборота 1 млрд ₽."

for channel in found_channels[:2]:
    context = f"Название: {channel['name']}\nСсылка: {channel['url']}\nПодписчики: {channel['subscribers']:,}\nОписание: {channel['description']}\nПоследнее видео: \"{channel['last_video_title']}\" ({channel['days_since_last_video']} дн. назад)"
    
    system_prompt = "Ты бренд-менеджер. Напиши оффер по модели PASTA (Personalization, Authority, Story, Terms, Action). Тон: дружелюбный, живой. Объем: 150-200 слов. ОБЯЗАТЕЛЬНО упомяни название последнего видео. Верни СТРОГО JSON с ключом 'offer_text'."
    user_prompt = f"{context}\n\nО бренде: {brand_info}\n\nЗАДАЧА: Напиши оффер."
    
    try:
        comp = groq_client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}], temperature=0.4, response_format={"type": "json_object"})
        clean = comp.choices[0].message.content.replace("```json", "").replace("```", "").strip()
        offer_text = json.loads(clean).get('offer_text', 'Ошибка')
        offers_results.append({'channel_name': channel['name'], 'channel_url': channel['url'], 'subscribers': channel['subscribers'], 'last_video': channel['last_video_title'], 'offer_text': offer_text})
    except Exception: pass

df_offers = pd.DataFrame(offers_results)
df_offers.to_excel(f"{ARTIFACTS_DIR}/youtube_outreach_offers.xlsx", index=False)
with open(f"{ARTIFACTS_DIR}/youtube_outreach_offers.json", 'w', encoding='utf-8') as f:
    json.dump(offers_results, f, ensure_ascii=False, indent=2)
print("✅ Проект успешно собран и сохранен!")
