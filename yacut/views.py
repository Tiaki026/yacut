from flask import Response, redirect, render_template

from settings import INDEX

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import validate_and_return, generate_short_link, create_short_link


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    """Главная страница."""
    form = URLMapForm()

    if form.validate_on_submit():
        original_link = form.original_link.data
        short_link = form.custom_id.data

        result = validate_and_return(short_link, form)
        if result:
            return result

        short_link = generate_short_link(short_link)
        return create_short_link(original_link, short_link, db, form)

    return render_template(INDEX, form=form)


@app.route('/<string:short_id>')
def redirect_short_to_original(short_id: str) -> Response:
    """Переадресация с короткой на длинную ссылку."""
    resutl = URLMap.query.filter_by(short=short_id).first_or_404().original

    return redirect(resutl)
