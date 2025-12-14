import json
from functools import lru_cache
from pathlib import Path
from aiogram.filters import BaseFilter
from aiogram.types import Message

LOCALES_PATH = Path("locales")


@lru_cache
def load_locale(lang: str) -> dict:
    file_path = LOCALES_PATH / f"{lang}.json"
    if not file_path.exists():
        file_path = LOCALES_PATH / "en.json"

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def t(lang: str, key: str) -> str:
    """
    Translate helper
    key example: 'buttons.add_report'
    """
    data = load_locale(lang)

    for part in key.split("."):
        data = data.get(part, {})

    return data if isinstance(data, str) else key



class I18nText(BaseFilter):
    def __init__(self, key: str):
        self.key = key

    async def __call__(self, message: Message, data: dict) -> bool:
        user = data.get("user")
        if not user:
            return False

        return message.text == t(user.lang, self.key)
