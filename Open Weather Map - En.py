# ================================== Imports =====================================
import datetime
import json
from requests import request
import requests 
from time import strftime
from tkinter import *
from tkinter import font, messagebox, ttk
from PIL import Image, ImageTk
import os

# =============================== Window Setting ==================================
window = Tk()
window.geometry("620x349+130+120")
window.title("Weather App")
window.resizable(False, False)

# ================================= Variables =====================================
system_Time = strftime("%H:%M:%S")
Hour = float(system_Time.split(":")[0])
Minute = int(system_Time.split(":")[1])

city = ""
city_Name = StringVar()
sky_Description_D = StringVar()
temp_D = IntVar()
humidity_D = IntVar()
wind_Speed_D = IntVar()

API_Key = "b80b9c6cfb48041a2190dde4b1024127"

# ================================ Background =====================================
if Hour == 00 or Hour == 01.0 or Hour == 02.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/00.jpg"))

elif Hour == 03.0 or Hour == 04.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/3.jpg"))

elif Hour == 05.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/5.jpg"))

elif Hour == 06.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/6.jpg"))

elif Hour == 07.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/7.jpg"))

elif Hour == 08.0:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/8.jpg"))

elif Hour == 09.0 or Hour == 10:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/9.jpg"))

elif Hour == 11 or Hour == 12:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/11.jpg"))

elif Hour == 13:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/13.jpg"))

elif Hour == 14 or Hour == 15:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/14.jpg"))

elif Hour == 16 or (Hour == 17 and Minute <= 30):
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/16.jpg"))

elif (Hour == 17 and Minute > 30) or (Hour == 18 and Minute <= 30):
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/17-30.jpg"))

elif Hour == 18 and Minute > 30:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/18-30.jpg"))

elif Hour == 19:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/19.jpg"))

elif Hour == 20:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/20.jpg"))

elif Hour == 21 or Hour == 22 or Hour == 23:
    BG_Img = ImageTk.PhotoImage(Image.open(
        str(os.getcwd()) + "\BG/21.jpg"))

background_label = Label(window, image=BG_Img)
background_label.pack(side="bottom", fill="both", expand="yes")

# =================================== Entries ====================================
city_Enter = Entry(background_label, width=13,
                   textvariable=city_Name, bd=2, font=("Arial", 15))
city_Enter.place(x=375, y=27)

# =================================== Labels =====================================
responce_City = Label(background_label, font=(19))
sky_Description_Label = Label(background_label, text="Sky Description:")
temp_Label = Label(background_label, text="Temperature:")
humidity_Label = Label(background_label, text="Humidity:")
wind_Speed_Label = Label(background_label, text="Wind Speed:")

sky_Description = Label(background_label)
temp = Label(background_label)
humidity = Label(background_label)
wind_Speed = Label(background_label)


CopyRight = Label(
    window, text="©2020 Esfandiar Kiani, All rights reserved.", font=("Arial", 7))
CopyRight.place(x=44, y=329)

# ================================= Functions =====================================


def Error_Box():
    messagebox.showerror("Invalid Value", "You Must Input A City Name . . . !")


def RunTime_Error():
    messagebox.showerror("Error", "An Error Occurred . . . !")


def weather_Data():
    global city
    global sky_Description_D
    global temp_D_U
    global humidity_D_P
    global wind_Speed_D_U

    city = city_Name.get().capitalize()
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=en&units=metric&appid={API_Key}"
    if city != "" or city != " ":
        # responce = request.get(URL)
        # print(responce.text)
        json_Responce = requests.get(URL).json()
        # json_Responce = responce.json()

        # print(responce)
        # print(json_Responce)

        SD_Cap = json_Responce["weather"][0]["description"]
        sky_Description_D = SD_Cap.capitalize()

        temp_D = json_Responce["main"]["temp"]
        temp_D_U = f"{temp_D} °C"

        humidity_D = json_Responce["main"]["humidity"]
        humidity_D_P = f"{humidity_D}%"

        wind_Speed_D = json_Responce["wind"]["speed"]
        wind_Speed_D_U = f"{wind_Speed_D} Km/h"
    else:
        Error_Box()


def GUI_Config():
    responce_City.configure(text=city)
    sky_Description.configure(text=sky_Description_D)
    temp.configure(text=temp_D_U)
    humidity.configure(text=humidity_D_P)
    wind_Speed.configure(text=wind_Speed_D_U)


def GUI_Place():
    responce_City.place(x=105, y=35)
    sky_Description_Label.place(x=35, y=110)
    temp_Label.place(x=35, y=160)
    humidity_Label.place(x=35, y=210)
    wind_Speed_Label.place(x=35, y=260)

    sky_Description.place(x=180, y=110)
    sky_Description.update()
    temp.place(x=180, y=160)
    temp.update()
    humidity.place(x=180, y=210)
    humidity.update()
    wind_Speed.place(x=180, y=260)
    wind_Speed.update()


def Search():
    try:
        weather_Data()
        GUI_Config()
        GUI_Place()
        window.update()
    except:
        RunTime_Error()


# =================================== Buttons ====================================
search = Button(background_label, bd=2, text="Search", command=Search)
search.place(x=425, y=66)


window.mainloop()
