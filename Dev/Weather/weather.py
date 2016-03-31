import subprocess
from urllib.request import urlopen
import json

def readText(text):
    subprocess.call(['picoTTS', text])

def readTextgTTS(text):
    subprocess.call(['google_speech', '-len', text])

def getWeather():
    f = urlopen('http://api.wunderground.com/api/CLE_A_INDIQUER/forecast10day/q/France/Marseille.json')
    data = f.read().decode('utf-8')
    f.close()
    parsed_json = json.loads(data)

    for weather_data in parsed_json['forecast']['txt_forecast']['forecastday']:
        if weather_data['pop'] == '60':
            print(weather_data['fcttext'])
            print('Avec SVOX Pico TTS...')
            readText(weather_data['fcttext'])
            print('Avec Google TTS...')
            readTextgTTS(weather_data['fcttext'])
            print('Fini!')
            break

if __name__ == '__main__':
    getWeather()
