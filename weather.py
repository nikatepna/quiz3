import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                                                       QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("temperature",self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel("weather",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key = "12736e7559d47076a6063bcb515bf99e"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        self.display_weather(data)




    def display_weather(self,data):

        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k - 273.15
        self.temperature_label.setText(f"{round(temperature_c)} °C")

        weather_description=data["weather"][0]["main"]
        self.description_label.setText(weather_description)

        if weather_description == "Clear":
            self.emoji_label.setText("🌞")
        elif weather_description == "Clouds":
            self.emoji_label.setText("☁️")
        elif weather_description == "Rain":
            self.emoji_label.setText("🌧️")
        elif weather_description == "Snow":
            self.emoji_label.setText("❄️")
        elif "storm" in weather_description or "thunder" in weather_description:
            self.emoji_label.setText("⛈️")
        elif weather_description == "Haze":
            self.emoji_label.setText("🌫️")
        else:
            self.emoji_label.setText("meti amindi agar vici")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
