from .forms import URLMapForm
from flask import render_template
from . import app


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm
    return render_template('index.html', form=form)
