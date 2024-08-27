from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


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
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                regex=r'^[a-zA-Z0-9]{6}$',
                message=(
                    'Будьте внимательны. \n'
                    'Можно использовать только латиницу с '
                    'заглавными и прописными буквами, а так же цифры.'
                )
            )
        ]
    )
    submit = SubmitField('Создать')
