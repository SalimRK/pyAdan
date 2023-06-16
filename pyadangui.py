import tkinter as tk
from customtkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

icon_path = "images/pyadaicon.ico"

# BeautifulSoup variables
response = requests.get("https://almaaref.org.lb/")
soup = BeautifulSoup(response.content, "html.parser")

# BeautifulSoup classes
date_class = "fw-bold"
imsak_class = "card mx-auto bg-warning text-light mb-1"
fajr_class = "card mx-auto bg-success text-light mb-1"
shorok_calss = "card mx-auto bg-info text-light mb-1"
dohor_class = "card mx-auto bg-primary text-light mb-1"
aser_class = "card mx-auto bg-danger text-light mb-1"
mogreb_class = "card mx-auto bg-secondary text-light mb-1"
esha_class = "card mx-auto bg-dark text-light mb-1"
mid_night_class = "card mx-auto bg-dark text-light mb-1"


def get_data(html_class):
    # Find the element with the specific class containing the date information
    data_element = soup.find(class_=html_class)  # Replace "your-class" with the appropriate class value
    # Extract the date text
    data_text = data_element.get_text(strip=True)
    return data_text


date_arb = f" مواقيــت الصـــلاة ليوم {get_data(date_class)} حسب توقيت مدينة بيروت "
date_arb = " ".join(date_arb.split()[::-1])
imsak_arb = "الإمساك"
fajr_arb = "الفجر"
shorok_arb = "الشروق"
dohor_arb = "الظهر"
aser_arb = "العصر"
mogreb_arb = "المغرب"
esha_arb = "العشاء"
mid_night_arb = "منتصف الليل"
mid_night_arb = " ".join(mid_night_arb.split()[::-1])

imsak_time = get_data(imsak_class)
fajr_time = get_data(fajr_class)
shorok_time = get_data(shorok_calss)
dohor_time = get_data(dohor_class)
aser_time = get_data(aser_class)
mogreb_time = get_data(mogreb_class)
esha_time = get_data(esha_class)
mid_night_time = get_data(mid_night_class)

# image variables
stop_food_img = CTkImage(Image.open(r"images/stop_food.png"))
morning_img = CTkImage(Image.open(r"images/morning.jpg"))
midday_img = CTkImage(Image.open(r"images/midday.jpg"))
evening_img = CTkImage(Image.open(r"images/evening.jpg"))
midnight_img = CTkImage(Image.open(r"images/midnight.jpg"))
refresh_img = CTkImage(Image.open(r"images/refresh.png"))


def refresh_clicked():
    pass


class MyFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_date_arb = CTkLabel(self, text=date_arb)
        self.label_imsak_time = CTkLabel(self, text=imsak_time)
        self.label_imsak_arb = CTkLabel(self, text=imsak_arb)
        self.image_imsak_pray = CTkLabel(self, text="", image=stop_food_img)
        self.label_fajr_time = CTkLabel(self, text=fajr_time)
        self.label_fajr_arb = CTkLabel(self, text=fajr_arb)
        self.image_morning_pray = CTkLabel(self, text="", image=morning_img)
        self.label_shorok_time = CTkLabel(self, text=shorok_time)
        self.label_shorok_arb = CTkLabel(self, text=shorok_arb)
        self.label_dohor_time = CTkLabel(self, text=dohor_time)
        self.label_dohor_arb = CTkLabel(self, text=dohor_arb)
        self.image_dohor_pray = CTkLabel(self, text="", image=midday_img)
        self.label_aser_time = CTkLabel(self, text=aser_time)
        self.label_aser_arb = CTkLabel(self, text=aser_arb)
        self.label_mogreb_time = CTkLabel(self, text=mogreb_time)
        self.label_mogreb_arb = CTkLabel(self, text=mogreb_arb)
        self.image_mogreb_pray = CTkLabel(self, text="", image=evening_img)
        self.label_esha_time = CTkLabel(self, text=esha_time)
        self.label_esha_arb = CTkLabel(self, text=esha_arb)
        self.label_mid_night_time = CTkLabel(self, text=mid_night_time)
        self.label_mid_night_arb = CTkLabel(self, text=mid_night_arb)
        self.image_mid_night_pray = CTkLabel(self, text="", image=midnight_img)

        self.label_date_arb.grid(row=0, column=0, padx=30, pady=10, columnspan=2)
        self.label_imsak_time.grid(row=1, column=0, padx=30, pady=10)
        self.label_imsak_arb.grid(row=1, column=1, padx=30, pady=10)
        self.image_imsak_pray.grid(row=1, column=2, padx=10)
        self.label_fajr_time.grid(row=2, column=0, padx=30, pady=10)
        self.label_fajr_arb.grid(row=2, column=1, padx=30, pady=10)
        self.image_morning_pray.grid(row=2, column=2, padx=10)
        self.label_shorok_time.grid(row=3, column=0, padx=30, pady=10)
        self.label_shorok_arb.grid(row=3, column=1, padx=30, pady=10)
        self.label_dohor_time.grid(row=4, column=0, padx=30, pady=10)
        self.label_dohor_arb.grid(row=4, column=1, padx=30, pady=10)
        self.image_dohor_pray.grid(row=4, column=2, padx=10)
        self.label_aser_time.grid(row=5, column=0, padx=30, pady=10)
        self.label_aser_arb.grid(row=5, column=1, padx=30, pady=10)
        self.label_mogreb_time.grid(row=6, column=0, padx=30, pady=10)
        self.label_mogreb_arb.grid(row=6, column=1, padx=30, pady=10)
        self.image_mogreb_pray.grid(row=6, column=2, padx=10)
        self.label_esha_time.grid(row=7, column=0, padx=30, pady=10)
        self.label_esha_arb.grid(row=7, column=1, padx=30, pady=10)
        self.label_mid_night_time.grid(row=8, column=0, padx=30, pady=10)
        self.label_mid_night_arb.grid(row=8, column=1, padx=30, pady=10)
        self.image_mid_night_pray.grid(row=8, column=2, padx=10)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("PyAdan")
        self.iconbitmap(icon_path)
        self.geometry("600x550")
        self.grid_columnconfigure(0, weight=1)

        self.refresh_button = CTkButton(self, command=refresh_clicked(), image=refresh_img)
        self.refresh_button.pack(pady=10)

        self.my_frame = MyFrame(master=self)
        self.my_frame.pack(padx=20, pady=20)


app = App()
app.mainloop()
