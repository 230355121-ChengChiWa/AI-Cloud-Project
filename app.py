from flask import Flask as fla, request, jsonify
from flask import render_template
import boto3

app=fla(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_max_data', methods=['GET'])
def get_max_data():
    client = boto3.client('forecastquery', region_name='us-east-1')
    forecast_arn='arn:aws:forecast:us-east-1:162690303242:forecast/forecast3_230355121'
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date') 
    filters = {
        "item_id" : "MAX"
    }

    response = client.query_forecast(
    ForecastArn=forecast_arn,
    StartDate=start_date,
    EndDate=end_date,
    Filters=filters
    )

    forecast_data = response['Forecast']['Predictions']

    return jsonify(forecast_data)

@app.route('/get_min_data', methods=['GET'])
def get_min_data():
    client = boto3.client('forecastquery', region_name='us-east-1')
    forecast_arn='arn:aws:forecast:us-east-1:162690303242:forecast/forecast3_230355121'
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date') 
    filters = {
        "item_id" : "MIN"
    }

    response = client.query_forecast(
    ForecastArn=forecast_arn,
    StartDate=start_date,
    EndDate=end_date,
    Filters=filters
    )

    forecast_data = response['Forecast']['Predictions']

    return jsonify(forecast_data)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)