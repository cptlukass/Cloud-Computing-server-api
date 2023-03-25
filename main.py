from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)


class Data(Resource):

    def get(self, city_name):
        response = requests.get('https://public-esa.ose.gov.pl/api/v1/smog')
        result = response.json()
        stored = []
        for i in result['smog_data']:
            if i['school']['city'] == city_name.upper():
                school_name = i['school']['name']
                street = i['school']['street']
                humidity = i['data']['humidity_avg']
                pressure = i['data']['pressure_avg']
                temperature = i['data']['temperature_avg']
                pm10 = i['data']['pm10_avg']
                pm25 = i['data']['pm25_avg']
                timestamp = i['timestamp']

                grouping = {'school_name': school_name, 'street': street, 'humidity': round(humidity, 2),
                            'pressure': round(pressure, 2), 'temperature': round(temperature, 2),
                            'pm10': round(pm10, 2), 'pm25': round(pm25, 2), 'timestamp': timestamp}
                stored.append(grouping)
        return stored


api.add_resource(Data, '/<city_name>')

if __name__ == "__main__":
    app.run(port=8001)
