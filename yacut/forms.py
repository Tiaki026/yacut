from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, Length, Optional, DataRequired
from settings import (
    MIN_LENGHT, MAX_SHORT_LENGTH,
    MAX_LONG_LENGHT, SUBMIT, REQUARED_FIELD
)
from .validators import validate_char_pool


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=REQUARED_FIELD),
            Length(min=MIN_LENGHT, max=MAX_LONG_LENGHT),
            URL()
        ]
    )
    custom_id = StringField(
        'Короткая ссылка',
        validators=[
            Length(min=MIN_LENGHT, max=MAX_SHORT_LENGTH),
            Optional(),
            validate_char_pool
        ]
    )
    submit = SubmitField(SUBMIT)
