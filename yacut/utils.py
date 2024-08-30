import random
from flask import flash, render_template
from http import HTTPStatus
from typing import Union
from settings import (
    CHAR_POOL, REQUIRED_FIELD, MAX_SHORT_LENGTH,
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


def create_link_in_db(db, url) -> None:
    """Создание записи в БД."""
    db.session.add(url)
    db.session.commit()


def api_add_url_utils(data) -> str:
    """Утилита для обработки логики API представления add_url."""
    if data is None:
        raise InvalidAPIUsage(WITHOUT_BODY, HTTPStatus.BAD_REQUEST)

    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD, HTTPStatus.BAD_REQUEST)

    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = get_unique_short_id()

    custom_url = data['custom_id']

    if len(custom_url) > MAX_SHORT_LENGTH or not char_pool(custom_url):
        raise InvalidAPIUsage(WRONG_NAME_SHORT_URL, HTTPStatus.BAD_REQUEST)

    if short_url(data['custom_id']):
        raise InvalidAPIUsage(URL_ALLREADY_EXIST, HTTPStatus.BAD_REQUEST)

    return custom_url


def api_get_url_utils(url) -> None:
    """Утилита для обработки логики API представления get_url."""
    if url is None:
        raise InvalidAPIUsage(WRONG_ID, HTTPStatus.NOT_FOUND)


def generate_short_link(short_link) -> str:
    """Генерация уникальной короткой ссылки, если она не была задана."""
    if not short_link:
        short_link = get_unique_short_id()
        while URLMap.query.filter_by(short=short_link).first():
            short_link = get_unique_short_id()

    return short_link


def create_short_link(original, short, db, form) -> str:
    """Создание новой короткой ссылки и добавление в базу данных."""
    url = URLMap(original=original, short=short)
    create_link_in_db(db, url)
    return render_template(
        INDEX,
        form=form,
        short_url=BASE_URL + url.short,
        original_link=url.original
    )


def validate_and_return(short_link: str, form) -> Union[str, None]:
    """Проверка короткой ссылки и возврат результата при ошибке."""
    if short_url(short_link):
        flash(URL_ALLREADY_EXIST)
        return render_template(INDEX, form=form)

    if short_link and not char_pool(short_link):
        flash(WRONG_NAME_SHORT_URL)
        return render_template(INDEX, form=form)

    return None
