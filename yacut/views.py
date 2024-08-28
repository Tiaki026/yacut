from .forms import URLMapForm
from flask import render_template, redirect
from . import app
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    # if form.validate_on_submit():

    return render_template('index.html', form=form)


@app.route('/<short_id>')
def redirect_short_to_original(url):
    """Переадресация с короткой на длинную ссылку."""
    return redirect(
        URLMap.query.filter_by(short=url).first_or_404().original
    )
