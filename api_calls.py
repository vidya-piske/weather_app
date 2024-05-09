import os
import requests
from dotenv import load_dotenv

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    elif response.status_code == 404:
        print("City not found. Please enter a valid city name.")
        return None
    else:
        print("Error fetching weather details")
        print("API response content:", response.content)
        return None

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    city_name = input("Enter city name:")
    api_key = os.getenv("API_KEY")
    weather = get_weather(city_name, api_key)
    
    if weather:
        print(f"Weather in {city_name}:")
        print(f"Description: {weather['description']}")     
        print(f"Temperature: {weather['temperature']}°C")     
        print(f"Humidity: {weather['humidity']}%")     
        print(f"Wind Speed: {weather['wind_speed']}m/s")     
    else:
        print("Weather data is not available")   
    
if __name__ == "__main__":
    main()
