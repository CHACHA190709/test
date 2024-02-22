from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QVBoxLayout, QPushButton
import requests


app = QApplication([])

window =QWidget()
window.setWindowTitle('Погода')
window.show()

layout = QVBoxLayout()

city = QLabel('Enter City:')
city_input = QLineEdit()
weather_button = QPushButton('Get Weather')
weather = QLabel('---')

layout.addWidget(city)
layout.addWidget(city_input)
layout.addWidget(weather_button)
layout.addWidget(weather)

window.setLayout(layout)

def get_weather():
    api_key = '451beccbae6d8abc1fe52150b044e522'
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    city = city_input.text()
    if not city:
        weather.setText('Please enter a city')
        return None

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        temp = data['main']['temp']
        weather.setText(f'Temperature in {city}: {temp} C')

    except:
        print('Error')

    
    
weather_button.clicked.connect(get_weather)

app.exec()