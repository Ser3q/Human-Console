# -*- coding: UTF-8 -*-
import speech_recognition as sr, webbrowser, pyttsx3, re, os, weather_script, datetime, winsound
from urllib.request import Request, urlopen
engine = pyttsx3.init()
mypos = ''
now = datetime.datetime.now()

def run():

    def recognize(text_r):

        if re.match('[Ww]łącz despacito', text_r):
            engine.say("Włączam")
            engine.runAndWait()
            print("Włączam.")
            webbrowser.open('https://www.youtube.com/watch?v=OD7AdmG9QfM', new=2)

        #Telling the time
        if re.match(".* godzin(a|ę)", text_r):
            print("Jest {}:{}".format(now.hour,now.minute))
            engine.say("Jest {}:{}".format(now.hour,now.minute))
            engine.runAndWait()

        #My localization
        if re.match("(lokalizacja|[\w ]* lokalizacj(a|ę)|[Gg]dzie jestem)", text_r):
            request = Request("https://www.google.com/search?hl=pl&safe=off&q=moja+lokalizacja")
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
            response = urlopen(request).read().decode("utf-8")
            mypos = re.findall(r'alt="Mapa: ((\d{2}-\d{3})|([\w,]+) ([\w ]+))', response)
            print("Twoja obecna lokalizacja to: " + mypos[0][3])
            engine.say("Twoja obecna lokalizacja to: " + mypos[0][3])
            engine.runAndWait()

        #My weather
        if re.match("(pogoda|(prognoza pogody)|([Cc]zy będzie padać))", text_r):
            weather_script.run(text_r)

        #My radio
        if re.match("\w* [Rr]adi(o|a)", text_r):
            engine.say("Włączam radio.")
            engine.runAndWait()
            webbrowser.open("https://www.antyradio.pl/sluchaj/online/Antyradio-online.html", new=2)

        #Open Calculator
        if re.match("\w* kalkulato(r|ra)", text_r):
            engine.say("Włączam kalkulator.")
            engine.runAndWait()
            os.system('calc.exe')


        #Open Browser
        if re.match("\w* przeglądark(a|ę|i)", text_r):
            webbrowser.open_new("https:\\www.google.pl")
            engine.say("Otwieram przeglądarkę")
            engine.runAndWait()

        #Search via Google
        if re.match("([Ww]yszukaj|[Zz]najdź|[Ss]zukaj) [\w \']", text_r):
            result = re.findall(r'([Ww]yszukaj|[Zz]najdź|[Ss]zukaj) ([\w \']*)', text_r)
            query = result[0][1]
            query = re.sub(r"\s+", '+', query)
            webbrowser.open("https://www.google.com/search?hl=pl&safe=off&q={}".format(query))
            engine.say("Szukam.")
            engine.runAndWait()


        #Open Website
        if re.match("([Oo]twórz stronę) [\w]+[\. ][\w]+", text_r):
            engine.say("Otwieram stronę.")
            engine.runAndWait()
            result = re.findall(r'([Oo]twórz stronę) ([\w]+[\. ][\w]+)', text_r)
            query = result[0][1]
            query = re.sub(r"\s+", '.', query)
            webbrowser.open("https://www.{}".format(query))

        #Creating directories
        if re.match("[Ss]twórz|[Uu]twórz (katalog|folder) [\w ]+", text_r):
            directory = re.findall("[Ss]twórz|[Uu]twórz (katalog|folder) ([\w ]+)", text_r)
            os.mkdir("C:\\Users\\Z510\\Desktop\\{}".format(directory[0][1]), 777)
            engine.say("Tworzę katalog.")
            engine.runAndWait()

        #Deleting directories
        if re.match("[Uu]suń (katalog|folder) [\w ]+", text_r):
            directory = re.findall("[Uu]suń (katalog|folder) ([\w ]+)", text_r)
            os.rmdir("C:\\Users\\Z510\\Desktop\\{}".format(directory[0][1]))
            engine.say("Usuwam katalog.")
            engine.runAndWait()


        #Creating note
        if re.match("[Nn]otatka|[Zz]anotuj [\w ]+", text_r):
            file = open("C:\\Users\\Z510\\Desktop\\Notatka {}-{}-{}.txt".format(now.day, now.month, now.year, now.ctime()), 'w+')
            ntext = re.findall("[Nn]otatka|[Zz]anotuj ([\w ]+)", text_r)
            file.write(ntext[0] + "\n")
            file.close()
            engine.say("Tworzę notatkę.")
            engine.runAndWait()

        #Opening program from our Desktop
        if re.match("[Ss]tart [\w ]+", text_r):
            exe = re.findall("[Ss]tart ([\w ]+)", text_r)
            os.startfile(r"C:\\Users\\Z510\\Desktop\\{}".format(exe[0]))
            engine.say("Otwieram program.")
            engine.runAndWait()

        #Opening file from our Desktop
        if re.match("[Oo]twórz plik [\w ]+", text_r):
            exe = re.findall("[Oo]twórz plik ([\w ]+)", text_r)
            exe = exe[0]
            exe = re.sub(" kropka ", ".", exe)
            print(exe)
            os.startfile(r"C:\\Users\\Z510\\Desktop\\{}".format(exe))
            engine.say("Otwieram plik.")
            engine.runAndWait()




    r = sr.Recognizer()

    engine.say("Co mogę dla Ciebie zrobić?")
    engine.runAndWait()

    with sr.Microphone() as source:

        print("Powiedz coś:")
        frequency = 1500
        duration = 500
        winsound.Beep(frequency, duration)
        #r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="pl-PL")
        print ("Powiedziałeś:")
        print (text)
        recognize(text)
    except:
        print("Nie zrozumiałam, co powiedziałeś, lub wystąpił błąd.")
        engine.say("Nie zrozumiałam, co powiedziałeś, lub wystąpił błąd.")
        engine.runAndWait()