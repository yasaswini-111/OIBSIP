import requests

print("=" * 40)
print("        WEATHER APPLICATION")
print("=" * 40)

api_key = "f36ac3aff4454ae6938164918261306"

while True:

    city = input("\nEnter City Name: ").strip()

    if city == "":
        print("City name cannot be empty.")
        continue

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("\nCity not found. Please enter a valid city.")
        else:
            location = data["location"]["name"]
            country = data["location"]["country"]
            temperature = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            condition = data["current"]["condition"]["text"]
            wind = data["current"]["wind_kph"]

            print("\n" + "=" * 40)
            print("             WEATHER REPORT")
            print("=" * 40)
            print(f"City          : {location}")
            print(f"Country       : {country}")
            print(f"Temperature   : {temperature} °C")
            print(f"Humidity      : {humidity}%")
            print(f"Condition     : {condition}")
            print(f"Wind Speed    : {wind} km/h")
            print("=" * 40)

    except requests.exceptions.RequestException:
        print("\nUnable to connect to the weather service.")

    choice = input("\nDo you want to search another city? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Weather Application.")
        break