import random
from settings import CHAR_POOL


def get_unique_short_id():
    """Создание короткой ссылки."""
    return ''.join(
        random.choices(CHAR_POOL, k=6)
    )
