# 03_generate_ideal_portrait.py
context_text = "\n---\n".join([f"Блогер: @{p['username']}\nБио: {p['bio']}\nКонтент: {' | '.join(p['recent_posts'])}" for p in profiles_data])

system_prompt = "Ты эксперт по influencer-маркетингу. Проанализируй данные и заполни предоставленный JSON-шаблон. КРИТИЧЕСКИ ВАЖНО: Используй ТОЛЬКО указанные 4 ключа."
user_prompt = f"Данные профилей:\n<data>\n{context_text}\n</data>\n\nЗаполни СТРОГО этот шаблон:\n{{\n  \"summary\": \"Краткое описание (2-3 предложения)\",\n  \"top_styles\": [\"стиль1\", \"стиль2\"],\n  \"top_topics\": [\"тема1\", \"тема2\"],\n  \"ideal_tone\": \"Описание тона\"\n}}"

try:
    comp = groq_client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}], temperature=0.1, response_format={"type": "json_object"})
    clean = comp.choices[0].message.content.replace("```json", "").replace("```", "").strip()
    ideal_portrait = IdealPortrait.model_validate_json(clean)
    
    with open(f"{ARTIFACTS_DIR}/ideal_portrait.json", "w", encoding="utf-8") as f:
        json.dump(ideal_portrait.model_dump(), f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Ошибка генерации портрета: {e}")
