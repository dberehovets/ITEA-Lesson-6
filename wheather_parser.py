from bs4 import BeautifulSoup as bs
import requests
from threading import Thread

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

base_url = "https://ua.sinoptik.ua"


def sin_parse(base_url, headers):
    request = requests.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        city = soup.find("div", attrs={"class": "cityName cityNameShort"}).text
        divs = soup.find_all("div", {"class": "main loaded"})
        for div in divs:
            temperature = div.find("div", attrs={"class": "temperature"}).text
            title = div.find("div")["title"]
            print(city[city.find("Погода"):])
            print(title)
            print(temperature[1:] if temperature[0] == " " else temperature)
    else:
        print("За введеними даними немає інформації")


def main():
    sin_parse(base_url, headers)
    location = input("Якщо ви бажаєте змінити місто, будь ласка, введіть його нижче. Для завершення програми натисніть Enter\n")
    if location == "":
        return
    date = input("""Введіть дату у форматі РРРР-ММ-ДД, на яку потрібно показати погоду, 
або просто натисніть Enter, щоб отримати погоду на сьогодні\n""")
    new_url = "https://ua.sinoptik.ua/погода-" + location + "/" + date
    t = Thread(target=sin_parse, args=(new_url, headers))
    t.start()


if __name__ == '__main__':
    main()



