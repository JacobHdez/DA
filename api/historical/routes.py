from flask import render_template
import pandas as pd

from api.historical import historical_bp


@historical_bp.route('/', methods=('GET',))
def index():
    df = pd.read_csv('api/static/f1_churn_predict_final.csv', parse_dates=['dtRef'])
    df['dtRef'] = df['dtRef'].dt.strftime('%Y %b %d')
    results = {
        date: group[['idDriver', 'f1Churn', 'proba']].to_dict('records')
        for date, group in df.groupby('dtRef')
    }
    all_drivers = sorted(df['idDriver'].unique())

    return render_template('historical.html', results=results, all_drivers=all_drivers)
