from datetime import datetime
from typing import Dict
from urllib.parse import urljoin

from flask import request

from settings import LONG_LENGHT_URL, SHORT_LENGTH_URL

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(LONG_LENGHT_URL), nullable=False)
    short = db.Column(db.String(SHORT_LENGTH_URL), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> Dict[str, str]:
        return {
            'url': self.original,
            'short_link': urljoin(request.url_root, self.short)
        }

    def from_dict(self, data) -> None:
        self.original = data.get('original', self.original)
        self.short = data.get('short', self.short)
