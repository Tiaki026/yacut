from flask import Response, redirect, render_template

from settings import INDEX

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import index_view_utils


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    """Главная страница."""
    form = URLMapForm()
    result = index_view_utils(form, db)

    if result:
        return result

    return render_template(INDEX, form=form)


@app.route('/<string:short_id>')
def redirect_short_to_original(short_id: str) -> Response:
    """Переадресация с короткой на длинную ссылку."""
    resutl = URLMap.query.filter_by(short=short_id).first_or_404().original

    return redirect(resutl)
