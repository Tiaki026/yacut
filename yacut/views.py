from flask import Response, flash, redirect, render_template

from settings import BASE_URL, INDEX, URL_ALLREADY_EXIST, WRONG_NAME_SHORT_URL

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import char_pool, get_unique_short_id, short_url


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    """Главная страница."""
    form = URLMapForm()

    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data

        if short_url(custom_id):
            flash(URL_ALLREADY_EXIST)
            return render_template(INDEX, form=form)

        if custom_id and not char_pool(custom_id):
            flash(WRONG_NAME_SHORT_URL)
            return render_template(INDEX, form=form)

        if not custom_id:
            custom_id = get_unique_short_id()
            while URLMap.query.filter_by(short=custom_id).first():
                custom_id = get_unique_short_id()

        url_map = URLMap(
            original=original_link,
            short=custom_id,
        )

        db.session.add(url_map)
        db.session.commit()

        return render_template(
            INDEX,
            form=form,
            short_url=BASE_URL+url_map.short,
            original_link=url_map.original
        )

    return render_template(INDEX, form=form)


@app.route('/<string:short_id>')
def redirect_short_to_original(short_id: str) -> Response:
    """Переадресация с короткой на длинную ссылку."""
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )
