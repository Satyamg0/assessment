from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API Key from Open Exchange Rates
API_KEY = 'c05067846a864c219fef9a997660877a'
BASE_URL = 'https://openexchangerates.org/api/latest.json'

# Endpoint for currency conversion

@app.route('/convert', methods=['https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currencyA}/{currencyB}.json'])
def convert_currency():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from_currency')
    to_currencies = request.args.getlist('to_currency')

    # Retrieve latest exchange rates
    params = {'app_id': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Convert amount to target currencies
    results = {}
    if from_currency in data['rates']:
        for target_currency in to_currencies:
            if target_currency in data['rates']:
                conversion_rate = data['rates'][target_currency]
                converted_amount = amount * conversion_rate
                results[target_currency] = converted_amount

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
