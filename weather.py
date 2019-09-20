import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


HEIGHT = 500
WIDTH = 600

def format_response(weather):
    print(weather)
    try: 
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        humidity = weather['main']['humidity']
        
        final_str = "City: %s \nCondition: %s \nTemperature (℉): %s \nLow-temperature (℉): %s \nHigh-temperature (℉): %s \nHumidity: %s" % (name, desc, temp, temp_min, temp_max, humidity)
    except:
        final_str = 'Invalid input, try again!'
        
    return final_str
        
def get_weather(zip):
    weather_key = '342ea63834e8756f0794172964696dc0'
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': weather_key, 'zip': zip, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label['text'] = format_response(weather)
    
    
def test_function(entry):
    print("This is the entry:", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="weather.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#000", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")


entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=('padmaa', 12), bg='#363534', fg= '#FE5100', justify='center',  command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#000', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='#363534', font=('Chilanka', 18), fg= '#FE5100', justify='center')
label.place(relwidth=1, relheight=1)

print(tk.font.families())

root.mainloop()