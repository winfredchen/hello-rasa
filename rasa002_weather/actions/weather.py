import requests

def Weather(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?APPID=460ab0c343925e35a26085ad9cff19bb&q='
    #city = input('enter the city name: ')
    url = api_address + city
    json_data = requests.get(url).json()

    format_add = json_data['main']
    print("weather is {0} temparature is min {1} celcius and max is {2} celcius".format(
        json_data['weather'][0]['main'],
        int(format_add['temp_min']-273),
        int(format_add['temp_max']-272)
    ))
    return format_add