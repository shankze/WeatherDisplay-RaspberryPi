import requests
import json
from datetime import datetime, timedelta
import tkinter as tk
import time

def getImageName(desc,icon):
    imageName = ''
    #clear
    if icon == '01d':
        return 'jclear_day.png'
    if icon == '01n':
        return 'jclear_night.png'
    #clouds
    if icon == '04d' or icon =='04n':
        return 'jcloudy.png'
    if icon == '02d' or icon=='03d':
        return 'jlcloud_day.png'
    if icon == '02n' or icon=='03n':
        return 'jlcloud_night.png'
    #rain
    if icon == '13d':
        return 'jfreezing_rain.png'
    if icon == '09d':
        return 'jshower_day.png'
    if icon == '09n':
        return 'jshower_night.png'
    if icon == '10d' or icon == '10n':
        if desc == 'light rain':
            return 'jlightrain.png'
        if desc == 'moderate rain':
            return 'jmoderaterain.png'
        else:
            return 'jheavyrain.png'
    #thunderstorm
    if icon == '11d' or icon =='11n':
        if desc == 'thunderstorm with light rain' or desc == 'thunderstorm with rain' or desc == 'light thunderstorm' or desc == 'thunderstorm with light drizzle':
            return 'jlight_thunderstorm.png'
        else:
            return 'jthunderstorms.png'
    #snow
    if icon == '13d' or icon == '13n':
        return 'jsnow.png'
    #haze
    if icon == '50d' or icon == '50n':
        return 'jfog.png'
    #default
    return 'jdefault.png'

class Images:
    def __init__(self):
        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.img4 = None
        self.img5 = None
        self.img6 = None
        self.img7 = None
        self.img8 = None

def getWeatherForecasts():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Houston,us&appid={API Key}&units=imperial'
    r = requests.get(url)
    parsed_string = json.loads(r.content.decode('utf-8'))
    city = parsed_string['city']['name']
    now = datetime.now()
    cont = True
    counter = 0
    valid_counter = 0
    forecasts = []
    while valid_counter < 10:
        forecast = []
        dtTime = parsed_string['list'][counter]['dt_txt']
        datetime_object = datetime.strptime(dtTime, '%Y-%m-%d %H:%M:%S')
        datetime_object_central = datetime_object - timedelta(hours=5, minutes=0)
        if datetime_object_central > now:
            formattedTime = '{0:%I %p}'.format(datetime_object_central)
            stFormattedTime = str(formattedTime)
            forecast.append(formattedTime.lstrip("0")) #0
            temp = int(parsed_string['list'][counter]['main']['temp'])
            forecast.append(str(temp)) #1
            forecast.append(parsed_string['list'][counter]['weather'][0]['description']) #2
            wspd = int(parsed_string['list'][counter]['wind']['speed'])
            forecast.append(str(wspd) + ' m/h') #3
            forecast.append(str(parsed_string['list'][counter]['weather'][0]['icon']))  # 4
            valid_counter = valid_counter + 1
        counter = counter + 1
        forecasts.append(forecast)
    return forecasts





def drawGrid():
    try:
        forecasts = getWeatherForecasts()


        forecast1 = forecasts[0]
        myImages.img1 = tk.PhotoImage(file=getImageName(forecast1[2], forecast1[4]))
        label_1_1 = tk.Label(window, image=myImages.img1, background="white").grid(row=0, column=0, padx=(00, 0),pady=(20, 0))
        label_1_2.config(text=forecast1[1])
        label_1_3.config(text=forecast1[2])
        label_1_4.config(text=forecast1[3])
        label_1_5.config(text=forecast1[0])

        forecast2 = forecasts[1]
        myImages.img2 = tk.PhotoImage(file=getImageName(forecast2[2],forecast2[4]))
        label_2_1 = tk.Label(window,image=myImages.img2,background="white").grid(row=0,column=1,padx=(00, 0),pady=(20,0))
        label_2_2.config(text=forecast2[1])
        label_2_3.config(text=forecast2[2])
        label_2_4.config(text=forecast2[3])
        label_2_5.config(text=forecast2[0])

        forecast3 = forecasts[2]
        myImages.img3 = tk.PhotoImage(file=getImageName(forecast3[2],forecast3[4]))
        label_3_1 = tk.Label(window,image=myImages.img3,background="white").grid(row=0,column=2,padx=(00, 0),pady=(20,0))
        label_3_2.config(text=forecast3[1])
        label_3_3.config(text=forecast3[2])
        label_3_4.config(text=forecast3[3])
        label_3_5.config(text=forecast3[0])


        forecast4 = forecasts[3]
        myImages.img4 = tk.PhotoImage(file=getImageName(forecast4[2],forecast4[4]))
        label_4_1 = tk.Label(window,image=myImages.img4,background="white").grid(row=0,column=3,padx=(00, 0),pady=(20,0))
        label_4_2.config(text=forecast4[1])
        label_4_3.config(text=forecast4[2])
        label_4_4.config(text=forecast4[3])
        label_4_5.config(text=forecast4[0])

        forecast5 = forecasts[4]
        myImages.img5 = tk.PhotoImage(file=getImageName(forecast5[2],forecast5[4]))
        label_5_1 = tk.Label(window,image=myImages.img5,background="white").grid(row=0,column=4,padx=(00, 0),pady=(20,0))
        label_5_2.config(text=forecast5[1])
        label_5_3.config(text=forecast5[2])
        label_5_4.config(text=forecast5[3])
        label_5_5.config(text=forecast5[0])

        forecast6 = forecasts[5]
        myImages.img6 = tk.PhotoImage(file=getImageName(forecast6[2],forecast6[4]))
        label_6_1 = tk.Label(window,image=myImages.img6,background="white").grid(row=0,column=5,padx=(00, 0),pady=(20,0))
        label_6_2.config(text=forecast6[1])
        label_6_3.config(text=forecast6[2])
        label_6_4.config(text=forecast6[3])
        label_6_5.config(text=forecast6[0])

        now = datetime.now()
        time.ctime()
        label_1_7.config(text="Last updated at: " +str(datetime.now().strftime('%A'))+ ' ' +str(datetime.now().strftime('%H:%M:%S %p' )))


    except Exception:
        pass

    window.after(1800000, drawGrid)

window = tk.Tk()
window.title("Houston - Forecast")
window.configure(background="white")
window.geometry('800x480')
window.grid_columnconfigure(12,minsize=180)
myImages = Images()
label_1_2 = tk.Label(window, background="white", font=("open sans", 44))
label_1_2.grid(row=1, column=0,padx=(00, 0), pady=(0, 0))
label_1_1 = tk.Label(window, image=myImages.img1, background="white")
label_1_1.grid(row=0, column=0, padx=(00, 0), pady=(20, 0))
label_1_2 = tk.Label(window, background = "white", font = ("open sans", 44))
label_1_2.grid(row=1, column=0, padx=(00, 0), pady=(0, 0))
label_1_3 = tk.Label(window, background="white", font=("open sans", 10))
label_1_3.grid(row=2, column=0, padx=(00, 0), pady=(00, 0))
label_1_4 = tk.Label(window,  background="white", font=("verdana", 10))
label_1_4.grid(row=3, column=0, padx=(00, 0), pady=(00, 0))
label_1_5 = tk.Label(window, background="white")
label_1_5.grid(row=4, column=0, padx=(00, 0), pady=(00, 0))
label_2_2 = tk.Label(window, background="white", font=("open sans", 44))
label_2_2.grid(row=1, column=1, padx=(00, 0), pady=(0, 0))
label_2_3 = tk.Label(window, background="white", font=("open sans", 10))
label_2_3.grid(row=2, column=1, padx=(00, 0), pady=(00, 0))
label_2_4 = tk.Label(window, background="white", font=("verdana", 10))
label_2_4.grid(row=3, column=1, padx=(00, 0), pady=(00, 0))
label_2_5 = tk.Label(window, background="white")
label_2_5.grid(row=4, column=1, padx=(00, 0), pady=(00, 0))
label_3_2 = tk.Label(window, background="white", font=("open sans", 44))
label_3_3 = tk.Label(window, background="white", font=("open sans", 10))
label_3_4 = tk.Label(window, background="white", font=("verdana", 10))
label_3_5 = tk.Label(window, background="white")
label_3_2.grid(row=1, column=2, padx=(00, 0), pady=(0, 0))
label_3_3.grid(row=2, column=2, padx=(00, 0), pady=(00, 0))
label_3_4.grid(row=3, column=2, padx=(00, 0), pady=(00, 0))
label_3_5.grid(row=4, column=2, padx=(00, 0), pady=(00, 0))
label_4_2 = tk.Label(window, background="white", font=("open sans", 44))
label_4_3 = tk.Label(window, background="white", font=("open sans", 10))
label_4_4 = tk.Label(window, background="white", font=("verdana", 10))
label_4_5 = tk.Label(window, background="white")
label_4_2.grid(row=1, column=3, padx=(00, 0), pady=(0, 0))
label_4_3.grid(row=2, column=3, padx=(00, 0), pady=(00, 0))
label_4_4.grid(row=3, column=3, padx=(00, 0), pady=(00, 0))
label_4_5.grid(row=4, column=3, padx=(00, 0), pady=(00, 0))
label_5_2 = tk.Label(window, background="white", font=("open sans", 44))
label_5_3 = tk.Label(window, background="white", font=("open sans", 10))
label_5_4 = tk.Label(window, background="white", font=("verdana", 10))
label_5_5 = tk.Label(window, background="white")
label_5_2.grid(row=1, column=4, padx=(00, 0), pady=(0, 0))
label_5_3.grid(row=2, column=4, padx=(00, 0), pady=(00, 0))
label_5_4.grid(row=3, column=4, padx=(00, 0), pady=(00, 0))
label_5_5.grid(row=4, column=4, padx=(00, 0), pady=(00, 0))
label_6_2 = tk.Label(window, background="white", font=("open sans", 44))
label_6_3 = tk.Label(window, background="white", font=("open sans", 10))
label_6_4 = tk.Label(window, background="white", font=("verdana", 10))
label_6_5 = tk.Label(window, background="white")
label_6_2.grid(row=1, column=5, padx=(00, 0), pady=(0, 0))
label_6_3.grid(row=2, column=5, padx=(00, 0), pady=(00, 0))
label_6_4.grid(row=3, column=5, padx=(00, 0), pady=(00, 0))
label_6_5.grid(row=4, column=5, padx=(00, 0), pady=(00, 0))
label_1_7 = tk.Label(window, background="white")
label_1_7.grid(column = 0,padx=(00,0),pady=(90,0),columnspan=2)
drawGrid()
window.mainloop()