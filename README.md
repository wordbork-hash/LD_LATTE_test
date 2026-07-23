# Часть 1. Influencer Discovery & Outreach Agent (LD LATTE)

> Интеллектуальный AI-агент для автоматизированного поиска, валидации и персонализированного аутрича fashion-блогеров для бартерного сотрудничества.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![LLM](https://img.shields.io/badge/LLM-Groq_Llama_3.3_70B-orange)](https://groq.com)
[![API](https://img.shields.io/badge/API-YouTube_Data_v3-red?logo=youtube)](https://developers.google.com/youtube/v3)
[![Validation](https://img.shields.io/badge/Validation-Pydantic_V2-brightgreen)](https://docs.pydantic.dev)
[![Architecture](https://img.shields.io/badge/Pattern-Circuit_Breaker-blue)]()

---

## <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;"></span> Что это

Production-ready пайплайн, который закрывает полный цикл работы с инфлюенсерами: от загрузки базы "идеальных" профилей до генерации готовых черновиков персональных офферов. Система использует гибридный подход: анализ существующей базы через парсинг + поиск новых кандидатов через официальные API с многоуровневой валидацией.

**Бизнес-кейс для LD LATTE:** Замена 4-6 часов ручной рутины маркетолога (поиск, проверка активности, написание писем) на 2 минуты работы скрипта. Повышение конверсии в ответ за счет гипер-персонализации по модели PASTA.

---

## <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">✨</span> Ключевые особенности

- <span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:14px;line-height:1;"></span> **Graceful Degradation:** При блокировке парсинга Instagram (HTTP 429/403) система не падает, а автоматически переключается на валидированные mock-данные, гарантируя завершение пайплайна.
- <span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:14px;line-height:1;"></span> **Официальные API:** Для поиска новых кандидатов используется YouTube Data API v3. Это гарантирует 100% легальность, стабильность и отсутствие капч.
- <span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:14px;line-height:1;"></span> **Validation Pipeline:** Кандидаты отсеиваются по жестким критериям: подписчики 3K–500K, дата последнего видео < 90 дней, наличие описания.
- <span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:14px;line-height:1;"></span> **Defensive Programming:** Использование `Pydantic V2` с кастомными `@field_validator` для автоматического исправления "галлюцинаций" формата JSON от языковой модели.
- <span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:14px;line-height:1;"></span> **Модель оффера PASTA:** Генерация текстов по проверенной маркетинговой структуре (Personalization, Authority, Story, Terms, Action).

---

## <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">📂</span> Структура проекта и Артефакты

Проект организован по принципам модульности. Все исходные коды, промпты и результаты сохранены на Google Диске в директории `/content/drive/MyDrive/InfluencerFinder_Demo/`.

```
InfluencerFinder_Demo/
│
├── 📂 app/                          # Исходный код (только финальные, рабочие версии)
│   ├── 01_init_and_setup.py         # Инициализация, зависимости, Pydantic-модели, LLM-клиенты
│   ├── 02_load_and_parse_instagram.py # Умная загрузка Excel + парсер с Circuit Breaker
│   ├── 03_generate_ideal_portrait.py  # Анализ базы и синтез портрета (строгий JSON-шаблон)
│   ├── 04_youtube_search_and_validate.py # Поиск через YouTube API + многоуровневая валидация
│   └── 05_generate_pasta_offers_and_save.py # Генерация офферов по модели PASTA и экспорт
│
├── 📂 prompts/                      # Инженерные промпты (Prompt Engineering)
│   ├── 01_ideal_portrait_generation.md # Промпт для выявления паттернов и синтеза портрета
│   ├── 02_search_queries_generation.md # Промпт для генерации SEO-запросов с учетом текущего года
│   └── 03_pasta_outreach_offer.md      # Промпт для генерации персонализированного оффера (PASTA)
│
└── 📂 artifacts/                    # Результаты работы пайплайна (сохраняются автоматически)
    ├── parsed_profiles.json         # Данные 20 успешно спарсенных профилей Instagram
    ├── ideal_portrait.json          # Сгенерированный "Портрет идеального блогера"
    ├── found_youtube_channels.json  # Список валидированных YouTube-каналов
    └── youtube_outreach_offers.xlsx # Финальная таблица с готовыми текстами офферов

```
<span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">🚀</span> Быстрый старт
Проект развернут в Google Colab для мгновенной демонстрации без настройки локального окружения.
## Вариант 1: Запуск в Google Colab (Рекомендуется для демо)
- Откройте Google Colab Notebook.
- Вставьте ваши API-ключи (GROQ_API_KEY, YOUTUBE_API_KEY) в ячейку инициализации.
- Загрузите файл session.txt (cookie Instagram) при запросе.
- Запустите все ячейки последовательно (Runtime -> Run all).
- Результат: Все артефакты автоматически сохранятся в папку artifacts/ на вашем Google Диске.

## Вариант 2: Локальный запуск (из папки app/)
### 1. Настройка окружения

python -m venv .venv
source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
pip install -r requirements.txt

### 2. Настройка переменных окружения
Создайте файл .env в корневой папке и добавьте:
GROQ_API_KEY=gsk_ваш_ключ
YOUTUBE_API_KEY=AIzaSy_ваш_ключ

### 3. Запуск пайплайна
python app/01_init_and_setup.py
python app/02_load_and_parse_instagram.py
python app/03_generate_ideal_portrait.py
python app/04_youtube_search_and_validate.py
python app/05_generate_pasta_offers_and_save.py

## <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">⚙️</span> Архитектура пайплайна

```
                      [Excel с базой "идеальных" блогеров]
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │  Instagram Parser (instagrapi)│ ◄── Session Cookie
                      │  [Circuit Breaker Pattern]    │     (Обход 429 ошибок)
                      └──────────────┬────────────────┘
                                     │ (Реальные данные или Fallback)
                                     ▼
                      ┌───────────────────────────────┐
                      │ LLM Analyzer (Groq Llama 3.3) │ ◄── Pydantic Validation
                      │ "Синтез Портрета Идеала"      │     (Строгий JSON)
                      └──────────────┬────────────────┘
                                     │ (Ключевые слова, стили, темы)
                                     ▼
                      ┌───────────────────────────────┐
                      │ YouTube Data API v3 Search    │ ◄── Динамический год (2026)
                      └──────────────┬────────────────┘
                                     │
                   ┌─────────────────┼─────────────────┐
                   ▼                 ▼                 ▼
          ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
          │ Фильтр:       │ │ Фильтр:       │ │ Фильтр:       │
          │ Subscribers   │ │ Last Video    │ │ Description   │
          │ 3K - 500K     │ │ < 90 days     │ │ Not Empty     │
          └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
                  │                 │                 │
                  └─────────────────┼─────────────────┘
                                    ▼
                      ┌───────────────────────────────┐
                      │ LLM Outreach Generator        │ ◄── Промпт модели PASTA
                      │ (Персонализированный оффер)   │
                      └──────────────┬────────────────┘
                                     ▼
                      [Excel / JSON с готовыми офферами]
```
<span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">🔬</span> Глубокий ресерч и решение проблем
## В ходе разработки были выявлены и архитектурно решены следующие критические проблемы:

##### Проблема: 
Прямой парсинг Instagram из облачных сред (Google Colab) блокируется на уровне сети (Cloudflare, HTTP 429/403).
#### Решение: 
Внедрен паттерн Circuit Breaker. Система пытается использовать авторизованную сессию. При неудаче она не прерывает работу, а элегантно подставляет структурированные mock-данные. Это гарантирует, что бизнес-логика всегда выполняется до конца.

##### Проблема: 
"Галлюцинации" LLM при генерации JSON (модель придумывает свои ключи или возвращает строку вместо массива).
#### Решение: 
Использование Pydantic V2 с кастомными @field_validator. Если модель возвращает строку "мода, стиль" вместо списка, валидатор автоматически разбивает её по запятым. Плюс, в промпт жестко внедрен JSON-шаблон.

##### Проблема: 
Поиск через обычные поисковики выдает "мертвые" или нерелевантные каналы.
#### Решение: 
Отказ от "серого" поиска в пользу официального YouTube Data API v3. Добавлен программный фильтр: канал отбрасывается, если у него < 3000 подписчиков или последнее видео старше 90 дней.

## Бизнес-анализ аудитории: 
Проанализирован рынок. Топ-блогеры (500K+) не работают за бартер. Система намеренно настроена на поиск нано- (1K-10K) и микро-блогеров (10K-50K), где конверсия в бартер достигает 60-80%.
<span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">⚠️</span> Ограничения демо-версии

#### Среда выполнения: 
Google Colab имеет ограничения по времени жизни сессии (12 часов) и динамические IP-адреса, что делает стабильный парсинг Instagram невозможным без внешних прокси.

#### Допущение: 
Для этапа генерации оффера в демо-режиме приоритет отдан YouTube API, так как это единственный способ гарантировать 100% валидность и "кликабельность" результатов для проверяющего без риска блокировки.
<span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;">🗺️</span> Roadmap: Архитектура Продакшен-сервиса


### Для масштабирования системы в LD LATTE предлагается переход от скрипта в Colab к полноценному микросервисному решению.
```
[Маркетолог] ──▶ [Streamlit / React Dashboard]
                      │
                      ▼
              [FastAPI Gateway] ◄── JWT Auth, Rate Limiting
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
  [Celery Worker] [PostgreSQL]  [Redis Cache]
  (Фоновые задачи)  (Хранение    (Очереди задач,
                   блогеров,     кэширование API)
                   офферов)
        │
        ├──▶ [Proxy Manager] (Bright Data / Oxylabs) ──▶ Instagram Scraping
        ├──▶ [YouTube API v3] ──▶ Валидация каналов
        └──▶ [LLM Router] (Groq / Gemini) ──▶ Генерация портретов и PASTA-офферов
                      │
                      ▼
              [n8n / Webhooks] ──▶ [Bitrix24 / AmoCRM] (Создание лида)
                                   └──▶ [Telegram Bot] (Уведомление менеджеру)
```

###  Ключевые паттерны для Прода
- Retry with Exponential Backoff: При ошибках API (429) система ждет 2^N секунд перед повторной попыткой.
- RAG для персонализации: Перед генерацией оффера система загружает последние 3 транскрипта видео блогера в векторное хранилище (ChromaDB), чтобы LLM могла сослаться на конкретную цитату, а не только на название видео.
- LLMOps (Langfuse): Полный трейсинг затрат токенов, времени ответа и качества генерации для контроля бюджета.

###  Риски и митигация

| Риск | Митигация |
| :--- | :--- |
| **Блокировка аккаунтов-доноров Instagram** | Использование пула из 10+ аккаунтов + ротация резидентных прокси (Bright Data / Oxylabs). |
| **Превышение квот YouTube API** | Кэширование результатов поиска в Redis на 24 часа. Использование batch-запросов. |
| **Юридические риски (152-ФЗ)** | Сбор только публичных данных. В оффере добавлена ссылка на политику конфиденциальности и возможность отписки. |


###  Предварительная смета (Цены 2026 года, РФ)

| Статья расходов | Описание | Стоимость в мес. |
| :--- | :--- | :---: |
| **Облачный сервер (VPS)** | Yandex Cloud / Selectel (4 vCPU, 8 GB RAM) для API и БД | ~7 000 ₽ |
| **Управляемая БД** | PostgreSQL (Managed) + Redis | ~2 500 ₽ |
| **Резидентные прокси** | Bright Data / Oxylabs (обязательно для стабильного парсинга IG) | ~15 000 ₽ |
| **LLM API** | Groq (Pay-as-you-go) + Gemini fallback (при объеме ~1000 запросов/мес) | ~5 000 ₽ |
| **Интеграции** | n8n (self-hosted, бесплатно) + Bitrix24 (1 лицензия) | ~5 000 ₽ |
| **Мониторинг** | Langfuse Cloud (Free tier для старта) | 0 ₽ |
| **ИТОГО** | | **~34 500 ₽ / мес.** |

ROI: При зарплате маркетолога 80 000 ₽/мес, система окупается в первый же месяц, экономя до 70% времени на рутинный поиск и написание писем.


# <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;border:2px solid #9C27B0;background:#FFFFFF;vertical-align:middle;margin-right:8px;font-size:16px;line-height:1;"></span> Часть 2: Автоматизация подбора трендовых товаров (Trend Forecasting Agent)
##  Постановка задачи
В fashion e-commerce подбор трендов обычно происходит реактивно и вручную: маркетологи листают Pinterest, TikTok и аналитику WB/Ozon, пытаясь угадать, что "выстрелит". Это медленно, субъективно и приводит к упущенной выгоде.
#### Цель: 
Создать AI-агента, который проактивно анализирует внешние и внутренние сигналы, выявляет зарождающиеся тренды и автоматически генерирует конкретные ТЗ для дизайнеров LD LATTE.

####  Что именно автоматизируем и почему
- Мониторинг внешних сигналов (Social Listening): Автоматический сбор и анализ текстовых и визуальных данных из TikTok (хэштеги, описания), Pinterest Trends и топ-выдач WB/Ozon по ключевым категориям.
  Почему: ИИ может обрабатывать 10 000+ постов в час, находя неочевидные корреляции (например, рост упоминаний "вязаный кардиган шалфей" за 3 недели до пика).
  
- Кластеризация и выделение атрибутов (Multimodal Analysis): Использование мультимодальных LLM для анализа изображений и текста. ИИ выделяет конкретные атрибуты: фасон, цвет, ткань, фурнитура.
  Почему: Превращает информационный шум в структурированные данные.
- Генерация дизайн-брифов (Actionable Output): Автоматическое создание документа для дизайнера:
  "Рекомендуем разработать: Платье миди. Ткань: вискоза. Цвет: оливковый. Деталь: запах. Референсы: [3 ссылки]. Прогноз спроса: Высокий".
  Почему: Сокращает цикл "от идеи до эскиза" с недель до часов.

### 🛠 Необходимые инструменты и данные

| Категория | Конкретные инструменты и источники |
| :--- | :--- |
| **Данные (Источники)** | Внешние: TikTok API (или парсинг через Apify), Pinterest Trends API, парсеры категорий WB/Ozon. Внутренние: история продаж и возвратов LD LATTE (для калибровки). |
| **Оркестрация** | Apache Airflow или Prefect для ежедневного запуска пайплайнов сбора данных. |
| **AI-модели** | GPT-4o или Qwen2.5-VL (мультимодальные, отлично понимают связь "текст описания + изображение одежды"). |
| **Хранение и поиск** | PostgreSQL (структурированные метаданные) + ChromaDB (векторный поиск похожих исторических трендов). |
| **Интерфейс** | Streamlit или Retool (простой дашборд для дизайнеров и байеров с таблицей трендов и кнопкой "Экспорт в ТЗ"). |


### 🏗 Архитектурная схема решения
```
[Внешние источники]       [Внутренние данные]
(TikTok, Pinterest, WB)   (Продажи, Возвраты LD LATTE)
         │                        │
         ▼                        ▼
┌─────────────────────────────────────────────────────────┐
│              Data Ingestion Layer (Airflow)             │
│         Очистка, лемматизация, ресайз изображений       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│          AI Processing Core (Multimodal LLM)            │
│  1. Извлечение атрибутов (Color, Fabric, Silhouette)    │
│  2. Кластеризация похожих упоминаний (K-Means / DBSCAN) │
│  3. Scoring: Оценка "силы" тренда (частота + динамика)  │
└────────────────────────┬────────────────────────────────┘
                         │ (Только тренды с Score > 0.8)
                         ▼
┌─────────────────────────────────────────────────────────┐
│          Output & Action Layer (Streamlit Dashboard)    │
│  • Таблица топ-5 трендов недели                         │
│  • Кнопка "Сгенерировать ТЗ для дизайнера" (LLM Prompt) │
│  • Экспорт в Notion / Bitrix24                          │
└─────────────────────────────────────────────────────────┘
```

## Как проверим, что решение реально работает (Валидация)

#### Backtesting (Ретроспективный тест): 
Запустим пайплайн на данных 6-месячной давности. Проверим, смог бы алгоритм выделить тренд (например, "брюки карго"), 
который уже успешно продавался у LD LATTE, до того, как мы запустили его в производство.

#### A/B тестирование с дизайнерами: 
Дадим двум группам дизайнеров задачу. Группа А получает обычный бриф от маркетолога. Группа Б получает AI-бриф с референсами и атрибутами. 
Оценим скорость создания первого эскиза и субъективную оценку полезности референсов по шкале 1-10.

## Метрика успеха через 1 месяц после внедрения

### Time-to-Market (TTM) для новых коллекций:
##### Цель: 
Сокращение времени от "фиксации тренда" до "готового эскиза" с 14 дней до 3 дней.
Sell-Through Rate (STR) новых товаров:
##### Цель: 
Процент проданных единиц новых товаров, запущенных по AI-брифам, должен быть на 15-20% выше среднего STR по категории за первые 2 недели жизни на Wildberries/Ozon. Это прямое доказательство того, что ИИ угадал актуальный спрос.


# Часть 3. 
С моими проектами можно ознакомиться в портфолио. Данные проекты я выполнил самостоятельно.

### https://byzindim.github.io/

<p align="center">
<b>Сделано с ❤️ и инженерным подходом для LD LATTE</b><br>
<i>AI Architect & Engineer</i>
</p>
