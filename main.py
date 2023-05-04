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
    if "ne haber" in voice:
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
        if "Yapay zeka güvenlik açıkları nelerdir ve nasıl önlenebilirler" in voice
            speak("Yapay zekâ, insanlar da dahil olmak üzere hayvanlar tarafından görüntülenen doğal zekânın aksine makineler tarafından görüntülenen zekâ çeşididir")
    if "Yapay zeka etik kuralları nelerdir" in voice
        speak("Eğitim ve farkındalık İnsan odaklı yaklaşım.Yapay zekada şeffaflık ve güvenliğe öncelik vermek")
    if "yapay zeka uygulamları hangi programlarla yazlır" in voice
                speak("c++,mattlab,lush,lisp,prolog,java")
        if"hiç okula gittinmi" in voice
            speak("ben bir yapay zekayım okula gidemem")
        if"kaç yaşındasın" in voice
            speak("ben bir yapay zekayım belirli bir yaşım yok")
        if"zaman neden sadece ileri akar" in voice
            speak("Termodinamiğin ikinci yasasına göre; ısı asla daha soğuk ve düşük enerjili bölgeden daha sıcak ve yüksek enerjili bir bölgeye akmaz. Yani entropi azalmaz. Yani düzensizlik azalmaz. Bu sebeple zaman da sürekli ileriye, düzensizliğe doğru tek yönde akar.")
        if"cinsiyetin nedir" in voice
            speak("ben bir yapay zeka olduğum için belirli bir cinsiyetim yok")
        if"ne zaman doğdun" in voice
            speak("ben bir yapay zeka olduğum için belirli bir doğum tarihim yok")
       
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