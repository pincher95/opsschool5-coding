from requests import get
import sys


def weather():
    if len(sys.argv) < 2:
        city_of_choice = "haifa"
    else:
        city_of_choice = sys.argv[1]
    city_weather = get(
        "http://api.weatherstack.com/current?access_key=dc8d23fb930a135acab4ae6d1af181da&query={}".format(
            city_of_choice))
    city_weather_json = city_weather.json()
    return ("The weather in {0} today {1} celsius".format(city_of_choice.capitalize(),
                                                          city_weather_json['current']['temperature']))


def main():
    print(weather())


if __name__ == '__main__':
    main()
