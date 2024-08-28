from settings import CHAR_POOL
from flask import flash, render_template
from .utils import get_unique_short_id


def validate_short_url(obj: str, form, url) -> str:
    """Валидация короткой ссылки: уникальность, длина и допустимые символы."""

    if obj and len(obj) > 6:
        flash('Это уже длинная ссылка, уложитесь в 6 символов.', 'warning')
        return render_template('index.html', form=form)

    if obj and not set(obj).issubset(CHAR_POOL):
        flash(
            'Будьте внимательны. \n'
            'Можно использовать только латиницу с '
            'заглавными и прописными буквами, а также цифры.',
            'warning'
        )
        return render_template('index.html', form=form)

    if url.query.filter_by(short=obj).first():
        flash(
            f'Ссылка {obj} уже кем-то занята.\nПопробуйте другой вариант.',
            'warning'
        )
        return render_template('index.html', form=form)

    if not obj:
        return get_unique_short_id()

    return obj
