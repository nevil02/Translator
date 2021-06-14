from tkinter import *
import tkinter as ttk
from googletrans import Translator as tx
from googletrans.client import Translator
import speech_recognition as sr
import pyttsx3 as tts
from gtts import gTTS
import os

#Translator
def convert_audio(s, d):
    translated_sentence = translator.translate(my_entry.get(1.0, "end-1c"),src=s,dest=d)
    speak = gTTS(text=translated_sentence.text, lang=d, slow= False)
    speak.save("captured_voice.mp3")
    os.system("start captured_voice.mp3")

def convert_text(s, d):
    translated_sentence = translator.translate(my_entry.get(1.0, "end-1c"),src=s,dest=d)
    my_entry2.configure(state="normal")
    my_entry2.delete('1.0', "end")
    my_entry2.insert(1.0,translated_sentence.text)
    my_entry2.configure(state="disabled")

map = {'Auto':'auto',
'Afrikaans':'af',
'Irish':'ga',
'Albanian':'sq',
'Italian':'it',
'Arabic':'ar',
'Japanese':'ja',
'Azerbaijani':'az',
'Kannada':'kn',
'Basque':'eu',
'Korean':'ko',
'Bengali':'bn',
'Latin':'la',
'Belarusian':'be',
'Latvian':'lv',
'Bulgarian':'bg',
'Lithuanian':'lt',
'Catalan':'ca',
'Macedonian':'mk',
'Chinese Simplified':'zh-CN',
'Malay':'ms',
'Chinese Traditional':'zh-TW',
'Maltese':'mt',
'Croatian':'hr',
'Norwegian':'no',
'Czech':'cs',
'Persian':'fa',
'Danish':'da',
'Polish':'pl',
'Dutch':'nl',
'Portuguese':'pt',
'English':'en',
'Romanian':'ro',
'Esperanto':'eo',
'Russian':'ru',
'Estonian':'et',
'Serbian':'sr',
'Filipino':'tl',
'Slovak':'sk',
'Finnish':'fi',
'Slovenian':'sl',
'French':'fr',
'Spanish':'es',
'Galician':'gl',
'Swahili':'sw',
'Georgian':'ka',
'Swedish':'sv',
'German':'de',
'Tamil':'ta',
'Greek':'el',
'Telugu':'te',
'Gujarati':'gu',
'Thai':'th',
'Haitian Creole':'ht',
'Turkish':'tr',
'Hebrew':'iw',
'Ukrainian':'uk',
'Hindi':'hi',
'Urdu':'ur',
'Hungarian':'hu',
'Vietnamese':'vi',
'Icelandic':'is',
'Welsh':'cy',
'Indonesian':'id',
'Yiddish':'yi'}


translator = Translator()

window = Tk()
window.title("My Translator")
window.geometry("1000x500")

label1 = Label(window, text="Enter text", font=("calibri",14))
label1.place(x=50,y=25)

my_entry = Text(window, font=("calibri", 14))
my_entry.pack(pady=20)
my_entry.place(height=300, width=400, x=50, y=50)

source = StringVar()
source.set("Auto")
drop1 = OptionMenu(window, source,"Afrikaans","Irish","Albanian","Arabic","Azerbaijani","Korean","Belarusian","Lithuanian","Macedonian","Chinese Simplified","Malay","Chinese Traditional","Maltese","Croatian","Norwegian","Czech","Danish","Polish","Dutch","Portuguese","English","Russian","Estonian","Filipino","Slovak","Finnish","Slovenian","French","Spanish","Swahili","Swedish","Tamil","Telugu","Gujarati","Thai","Turkish","Hebrew","Ukrainian","Hindi","Urdu","Hungarian","Vietnamese","Icelandic","Welsh","Indonesian","Yiddish")
drop1.pack(pady=20)
drop1.place(width=200,x=150, y=400)

label2 = Label(window, text="Translation", font=("calibri",14))
label2.place(x=550,y=25)

my_entry2 = Text(window, font=("calibri", 14))
my_entry2.pack(pady=20)
my_entry2.place(height=300, width=400, x=550, y=50)
my_entry2.configure(state="disabled")

desti = StringVar()
desti.set("Hindi")
drop2 = OptionMenu(window, desti,"Afrikaans","Irish","Albanian","Arabic","Azerbaijani","Korean","Belarusian","Lithuanian","Macedonian","Chinese Simplified","Malay","Chinese Traditional","Maltese","Croatian","Norwegian","Czech","Danish","Polish","Dutch","Portuguese","English","Russian","Estonian","Filipino","Slovak","Finnish","Slovenian","French","Spanish","Swahili","Swedish","Tamil","Telugu","Gujarati","Thai","Turkish","Hebrew","Ukrainian","Hindi","Urdu","Hungarian","Vietnamese","Icelandic","Welsh","Indonesian","Yiddish")
drop2.pack(pady=20)
drop2.place(width=200,x=650, y=400)

speak_button = Button(window, text="Speak", command=lambda:convert_audio(map[source.get()], map[desti.get()]))
speak_button.pack(pady=20)
speak_button.place(width=100,x=450,y=380)

text_button = Button(window, text="Text", command=lambda:convert_text(map[source.get()], map[desti.get()]))
text_button.pack(pady=20) 
text_button.place(width=100,x=450,y=420)



window.mainloop()