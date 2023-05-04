from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os


r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            speak('sistem çalışmıyor')
        return voice

def response(voice):
    if  "ne haber" in voice:
        speak('iyiyim sen nasılsın')
    if "nasılsın" in voice:
            speak('iyiyim sen nasılsın')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record("ne aramak istiyorsunuz")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
    if 'kapan' in voice:
        speak('görüşürüz')
        exit()
    if "Sen kimsin" in voice:
        speak("Ben Bir Yapay Zekayım Ve Adım Ela")
    if "Yapabileceğin şeyler ne" in voice:
        speak("Bana Yapay Zeka İle Sorular Sorabilirsiiniz Google De Arama Yaptırabilirsiniz ve Saati Sorabilirsiniz")
    if "Bu Sene Kim sampiyon olcak" in voice:
        speak("Tahmin etmek zor gibi ama iyi olan kazanmasını isterim")
    if "2 artı 2" in voice:
        speak("dört")
    if "şarkı aç" in voice:
        search = record("Şarkıyı Açayımmı")
        url = 'https://www.youtube.com/watch?v=cT3-_rz1cSA' + search
        webbrowser.get().open(url)
        speak("Şarkı Açılıyor")

    if "Yapay zeka nedir  nasıl çalışır" in voice:
           speak(" yapay zeka farklı yöntem ve teknolojiler ile birlikte çalışır.")


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Merhaba Ben ela Nasıl yardımcı olabilirim')
while True:
    voice = record()
    print(voice)
    response(voice)