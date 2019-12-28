from requests import get
import sys


def print_result(city, metric):
    query_params = {
        'access_key': "dc8d23fb930a135acab4ae6d1af181da",
        'query': city,
        'units': metric[1]
    }
    api_request = get('http://api.weatherstack.com/current', query_params)
    api_request_json = api_request.json()
    if "error" in api_request_json:
        print("City {} not found try:\n- Haifa\n- Paris\n- Moscow".format(city))
        return
    else:
        print("The weather in {0} today {1} {2}".format(api_request_json['location']['name'],
                                                        api_request_json['current']['temperature'],
                                                        metric[0]))
        return


def weather():
    cities_metric_query = [arg.split() for arg in ' '.join(sys.argv[1:]).split(",")]
    metric = [0]
    for city_metric in cities_metric_query:
        if len(city_metric) < 2:
            metric = ["Celsius", "m"]
        elif city_metric[1] == "-f":
            metric = ["Fahrenheit", "f"]
        else:
            metric = ["Celsius", "m"]
        print_result(city_metric[0], metric)
    return


def main():
    weather()


if __name__ == '__main__':
    main()
