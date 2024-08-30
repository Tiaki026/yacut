from typing import Literal

from flask import Response, jsonify, request
from http import HTTPStatus

from . import app, db
from .models import URLMap
from .utils import api_get_url_utils, api_add_url_utils, create_link_in_db


@app.route('/api/id/', methods=['POST'])
def add_url() -> tuple[Response, Literal[HTTPStatus.CREATED]]:
    """Короткая ссылка API."""

    data = request.get_json(silent=True)
    custom_url = api_add_url_utils(data)
    url = URLMap(original=data['url'], short=custom_url)
    create_link_in_db(db, url)

    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id) -> tuple[Response, Literal[HTTPStatus.OK]]:
    """Длинная ссылка API."""
    url = URLMap.query.filter_by(short=short_id).first()
    api_get_url_utils(url)

    return jsonify({'url': url.original}), HTTPStatus.OK
