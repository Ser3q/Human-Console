import re, pyttsx3
from urllib.request import Request, urlopen
from weather import Unit, Weather
engine = pyttsx3.init()
def run(text_r):
    if re.match("(pogoda|(prognoza pogod(a|ę|y))|([Cc]zy)? będzie padać)", text_r):
        request = Request("https://www.google.com/search?hl=pl&safe=off&q=moja+lokalizacja")
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
        response = urlopen(request).read().decode("utf-8")
        mypos = re.findall(r'alt="Mapa: ((\d{2}-\d{3})|([\w,]+) ([\w ]+))', response)
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location('{}'.format(mypos[0][3]))
        condition = location.condition
        forecast = "Prognoza na dziś:\n"
        if (condition.text == "Heavy Rain"):
            forecast += "Silne opady deszczu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Rain"):
            forecast += "Opady deszczu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Showers"):
            forecast += "Przelotne opady deszczu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Cloudy"):
            forecast += "Pochmurno.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Partly Cloudy"):
            forecast += "Częściowe zachmurzenie.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Blowing Snow"):
            forecast += "Pada śnieg.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Blustery"):
            forecast += "Dżdżysto.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Clear"):
            forecast += "Bezchmurnie.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Cold"):
            forecast += "Chłodno.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Drizzle"):
            forecast += "Mżawka.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Fair"):
            forecast += "Pogodnie.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Freezing Drizzle"):
            forecast += "Zamarzająca mżawka.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Freezing Rain"):
            forecast += "Zamarzający deszcz.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Foggy"):
            forecast += "Mglisto.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Hail"):
            forecast += "Grad.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Haze"):
            forecast += "Mgła.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Heavy Snow"):
            forecast += "Obfite opady śniegu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Hot"):
            forecast += "Gorąco.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Hurricane"):
            forecast += "Ryzyko huraganu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Isolated Thundershowers" or "Isolated Thunderstorms"):
            forecast += "Pojedyncze burze.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Light Snow Showers"):
            forecast += "Lekkie opady śniegu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Mixed Rain and Hail"):
            forecast += "Deszcz z gradem.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Mixed Rain and Sleet" or "Mixed Rain and Snow"):
            forecast += "Deszcz ze śniegiem.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Mostly Cloudy"):
            forecast += "Głównie pochmurno.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Scattered Showers"):
            forecast += "Przelotne opady deszczu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Scattered Thunderstorms"):
            forecast += "Przelotne burze.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Severe Thunderstorms"):
            forecast += "Burze z piorunami.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Sleet"):
            forecast += "Śnieg z deszczem.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Smoky"):
            forecast += "Kiepska jakość powietrza.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Snow"):
            forecast += "Śnieg.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Snow Flurries"):
            forecast += "Lekkie opady śniegu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Snow Showers"):
            forecast += "Przelotne opady śniegu.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Sunny"):
            forecast += "Słonecznie.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Thundershowers"):
            forecast += "Burze.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Thunderstorms"):
            forecast += "Burze z piorunami.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Tornado"):
            forecast += "Ryzyko tornada.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Tropical Storm"):
            forecast += "Burza tropikalna.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        elif (condition.text == "Windy"):
            forecast += "Wietrznie.\nTemperatura: " + condition.temp + " stopni Celsjusza."
        print(forecast)
        engine.say(forecast)
        engine.runAndWait()
