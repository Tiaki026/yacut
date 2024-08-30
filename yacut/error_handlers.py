from typing import Dict, Literal, Tuple

from flask import Response, jsonify, render_template
from http import HTTPStatus

from . import app, db


class InvalidAPIUsage(Exception):
    """Исключения API."""
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> Dict[str, str]:
        """Метод для сериализации переданного сообщения об ошибке."""
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error) -> Tuple[Response, int]:
    """Обработчик кастомного исключения для API."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error) -> tuple[Response, Literal[HTTPStatus.NOT_FOUND]]:
    """Обработчик ошибки 404."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(500)
def internal_error(error) -> tuple[Response, Literal[HTTPStatus.BAD_GATEWAY]]:
    """Обработчик ошибки 500."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.BAD_GATEWAY
