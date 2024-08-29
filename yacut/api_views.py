from typing import Literal

from flask import Response, jsonify, request

from . import app, db
from .models import URLMap
from .utils import api_add_url_utils, api_get_url_utils


@app.route('/api/id/', methods=['POST'])
def add_url() -> tuple[Response, Literal[201]]:
    """Короткая ссылка API."""

    data = request.get_json(silent=True)
    custom_id = api_add_url_utils(data)
    url = URLMap(original=data['url'], short=custom_id)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id) -> tuple[Response, Literal[200]]:
    """Длинная ссылка API."""
    url = URLMap.query.filter_by(short=short_id).first()
    api_get_url_utils(url)
    return jsonify({'url': url.original}), 200
