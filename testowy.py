from urllib.request import Request, urlopen
from weather import Unit, Weather
engine = pyttsx3.init()
text_r="pogoda"
def run(text_r):
    if re.match("(pogoda|(prognoza pogod(a|ę|y))|([Cc]zy)? będzie padać)", text_r):
        print('działam')
        request = Request("https://www.google.com/search?hl=pl&safe=off&q=moja+lokalizacja")
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
        response = urlopen(request).read().decode("utf-8")
        mypos = re.findall(r'alt="Mapa: ((\d{2}-\d{3})|([\w,]+) ([\w ]+))', response)
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location('{}'.format(mypos[0]))
        condition = location.condition
        forecast = "Prognoza na dziś:\n"