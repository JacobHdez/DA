from flask import render_template
import pandas as pd

from api.historical import historical_bp


@historical_bp.route('/', methods=('GET',))
def index():
    df = pd.read_csv('api/static/f1_churn_predict_final.csv', parse_dates=['dtRef'])
    results = {
        date: group[['idDriver', 'f1Churn']].to_dict('records')
        for date, group in df.groupby('dtRef')
    }

    return render_template('historical.html', results=results)
