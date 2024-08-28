import random

from settings import CHAR_POOL

from .models import URLMap


def get_unique_short_id() -> str:
    """Создание короткой ссылки."""
    return ''.join(
        random.choices(CHAR_POOL, k=6)
    )


def char_pool(objs: str) -> bool:
    """Заготовка для проверки коротких ссылок."""
    return set(objs).issubset(CHAR_POOL)


def short_url(obj: str) -> str:
    """Проверка существующей короткой ссылки в базе."""
    if URLMap.query.filter_by(short=obj).first():
        return obj
