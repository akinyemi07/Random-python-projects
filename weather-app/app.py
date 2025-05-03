from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'City not provided'}), 400

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code != 200 or forecast_response.status_code != 200:
        return jsonify({'error': 'City not found'}), 404

    weather_data = weather_response.json()
    forecast_data = forecast_response.json()

    return jsonify({
        'current': weather_data,
        'forecast': forecast_data['list'][:5]
    })

if __name__ == '__main__':
    app.run(debug=True)

