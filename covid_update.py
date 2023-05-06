import requests
import json
import time
from win10toast import ToastNotifier


def update():
    r = requests.get("https://api.covidtracking.com/v1/us/current.json")
    data = r.json()[0]

    print(data, type(data))
    text = f"Confirmed Cases : {data['positive']} \nDeaths : {data['death']} \nRecovered : {data['negative']}"
    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Update", text, duration=10)
        time.sleep(10000)


update()
