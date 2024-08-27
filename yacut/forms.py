# Опишите форму и валидаторы полей форм. Форма должна содержать поля:
# original_link — поле для оригинальной длинной ссылки,
# custom_id — поле для пользовательского варианта короткого идентификатора.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class YacutForm(FlaskForm):
    original_link = StringField(
        'Ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Короткая ссылка',
        validators=[Length(1, 16)]
    )
    submit = SubmitField('Создать')
