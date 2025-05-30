from flask import render_template

from api.historical import historical_bp


@historical_bp.route('/', methods=('GET',))
def index():
    return render_template('historical.html')
