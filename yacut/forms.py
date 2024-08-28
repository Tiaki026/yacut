from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
            URL()
        ]
    )
    custom_id = StringField(
        'Короткая ссылка',
        validators=[Length(1, 16), Optional()])
    submit = SubmitField('Создать')
