import requests
import json


print("Welcome to the Weather App! Please choose from the menu below: \n")


user_city = None
user_zip = None


def get_weather_data(city=user_city, zip=user_zip):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    apiid = "97e513ed6dda1b884d8efd4063736b2c"
    if zip is not None:
        base_url += "&zip=" + str(zip) + ",us"
    else:
        base_url += "q=" + str(city)

    base_url += "&units=imperial&appid=" + str(apiid)
    req = requests.get(base_url)
    return req


def weather_output(response):
    if response.status_code == 200:
        data = response.json()
        print(f"""{data['name']} Weather Forecast:
        Type: {data['weather'][0]['description']}
        Wind Speed : {data['wind']['speed']} miles/hr
        Visibility : {data['visibility']} m
        Temperature : {data['main']['temp']} F
        Humidity : {data['main']['humidity']} %
        """)
    else:
        print("Request for weather failed. Error : ", response.status_code)


def main():
    while True:

        user_selection = input("1.) Enter City Name. \n2.) Enter Zip Code. \n3.) Quit.\n #: ")

        if user_selection == "1":
            try:
                user_city = input("Enter City: ")
                response = get_weather_data(user_city, None)
                print("\nConnection to server successful...\n")
                weather_output(response)
            except Exception as err:
                print("Error: ", err)
        elif user_selection == "2":
            try:
                user_zip = input("Enter Zip Code: ")
                response = get_weather_data(None, user_zip)
                print("\nConnection to server successful...\n")
                weather_output(response)
            except Exception as err:
                print("Error: ", err)
        elif user_selection == 3:
            print("Thank you for using Weather App. Goodbye!")
            exit()
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
