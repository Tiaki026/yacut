from typing import Literal

from flask import Response, jsonify, request

from settings import (
    REQUIRED_FIELD, SHORT_LENGTH_URL, URL_ALLREADY_EXIST,
    WITHOUT_BODY, WRONG_ID, WRONG_NAME_SHORT_URL
)

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import char_pool, get_unique_short_id, short_url


@app.route('/api/id/', methods=['POST'])
def add_url() -> tuple[Response, Literal[201]]:
    """Короткая ссылка API."""
    data = request.get_json(silent=True)

    if data is None:
        raise InvalidAPIUsage(WITHOUT_BODY, 400)

    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD, 400)

    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = get_unique_short_id()
    custom_id = data['custom_id']
    if len(custom_id) > SHORT_LENGTH_URL or not char_pool(custom_id):
        raise InvalidAPIUsage(WRONG_NAME_SHORT_URL, 400)

    if short_url(custom_id):
        raise InvalidAPIUsage(URL_ALLREADY_EXIST, 400)

    url = URLMap(original=data['url'], short=custom_id)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id) -> tuple[Response, Literal[200]]:
    """Длинная ссылка API."""
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage(WRONG_ID, 404)
    return jsonify({'url': url.original}), 200
