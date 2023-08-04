from gtts import gTTS
from googletrans import Translator
translator = Translator()
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
# print("Insert your text:")
# mytext_origin = input()
mytext_origin = 'Deci, la fiecare 5 minute, botul va introduce acest link și va reîmprospăta datele.De fiecare dată când va introduce acest link și va prelua datele, trebuie să le salveze într-un fișier txt.'# here you can change the text
mytext = translator.translate(mytext_origin, dest='ro').text  
# Language in which you want to convert
language = 'ro'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False, tld='co.uk')
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")    