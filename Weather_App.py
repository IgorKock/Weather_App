import requests
import tkinter as tk
from tkinter import messagebox

# Function to get the weather forecast
def get_forecast(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    #url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        request = requests.get(url)
        request.raise_for_status()  # Opens a exception for the requesition errors

        data = request.json()

        if data["cod"] != 200:
            raise ValueError("City not found.")

        # Getting the information of the JSON that was returned
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        # Show the information on the GUI
        result_var.set(f"Temperature: {temperature}°C\n"
                       #f"Temperature: {temperature}°F\n"
                          f"Description: {description}\n"
                          f"Humidity: {humidity}%\n"
                          f"Wind: {wind} m/s")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Requesition Error: {e}")
    except ValueError as e:
        messagebox.showerror("Error", f"{e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error ocurred: {e}")


# Function called when the search button is clicked
def search_forecast():
    city = city_entry.get()
    api_key = ""  # Add your OpenWeatherMap API key here
    if city:
        get_forecast(city, api_key)
    else:
        messagebox.showwarning("Warning", "Please, put a city name here.")


# Creating the window
root = tk.Tk()
root.title("Weather Forecast")

# Creating widgets
titles_label = tk.Label(root, text="Weather Forecast", font=("Arial", 16))
titles_label.pack(pady=10)

city_label = tk.Label(root, text="City Name:", font=("Arial", 12))
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", font=("Arial", 12), command=search_forecast)
search_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
