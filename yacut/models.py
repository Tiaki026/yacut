from datetime import datetime, UTC

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(1, 256), nullable=False)
    short = db.Column(db.String(1, 16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(UTC))
