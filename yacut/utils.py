import random
from flask import flash, render_template
from typing import Union
from settings import (
    CHAR_POOL, REQUIRED_FIELD, SHORT_LENGTH_URL,
    URL_ALLREADY_EXIST, WITHOUT_BODY,
    WRONG_NAME_SHORT_URL, WRONG_ID, INDEX, BASE_URL
)

from .error_handlers import InvalidAPIUsage
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


def api_add_url_utils(data) -> str:
    """Утилита для обработки логики API представления add_url."""
    if data is None:
        raise InvalidAPIUsage(WITHOUT_BODY, 400)

    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD, 400)

    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = get_unique_short_id()

    custom_url = data['custom_id']

    if len(custom_url) > SHORT_LENGTH_URL or not char_pool(custom_url):
        raise InvalidAPIUsage(WRONG_NAME_SHORT_URL, 400)

    if short_url(data['custom_id']):
        raise InvalidAPIUsage(URL_ALLREADY_EXIST, 400)

    return custom_url


def api_get_url_utils(url):
    """Утилита для обработки логики API представления get_url."""
    if url is None:

        raise InvalidAPIUsage(WRONG_ID, 404)


def index_view_utils(obj, db) -> Union[str, None]:
    """Утилита для обработки логики представления index_view."""
    if obj.validate_on_submit():

        original_link = obj.original_link.data
        short_link = obj.custom_id.data

        if short_url(short_link):
            flash(URL_ALLREADY_EXIST)
            return render_template(INDEX, form=obj)

        if short_link and not char_pool(short_link):
            flash(WRONG_NAME_SHORT_URL)
            return render_template(INDEX, form=obj)

        if not short_link:
            short_link = get_unique_short_id()
            while URLMap.query.filter_by(short=short_link).first():
                short_link = get_unique_short_id()

        url_map = URLMap(
            original=original_link,
            short=short_link,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            INDEX,
            form=obj,
            short_url=BASE_URL+url_map.short,
            original_link=url_map.original
        )

    return None
