# 01_init_and_setup.py
import os
import json
import pandas as pd
import time
from datetime import datetime, timezone
from google.colab import drive
from pydantic import BaseModel, Field, field_validator
from typing import List
from groq import Groq
from google import genai
from googleapiclient.discovery import build

# Монтирование диска
drive.mount('/content/drive')

# Пути
BASE_DIR = "/content/drive/MyDrive/InfluencerFinder_Demo"
ARTIFACTS_DIR = f"{BASE_DIR}/artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# API Ключи (ВСТАВИТЬ СВОИ)
os.environ["GROQ_API_KEY"] = "gsk_ВАШ_КЛЮЧ"
os.environ["YOUTUBE_API_KEY"] = "AIzaSy_ВАШ_КЛЮЧ"

# Инициализация клиентов
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
youtube = build('youtube', 'v3', developerKey=os.environ.get("YOUTUBE_API_KEY"))

# Pydantic модели
class IdealPortrait(BaseModel):
    summary: str = "Не указано"
    top_styles: List[str] = []
    top_topics: List[str] = []
    ideal_tone: str = "Не указано"

    @field_validator('top_styles', 'top_topics', mode='before')
    @classmethod
    def fix_lists(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.replace('\n', ',').split(',') if x.strip()]
        if isinstance(v, list):
            return [str(x).strip() for x in v if str(x).strip()]
        return []
