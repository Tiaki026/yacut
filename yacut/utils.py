import random
import string


def get_unique_short_id():
    """Создание короткой ссылки."""
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )
