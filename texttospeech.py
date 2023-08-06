from gtts import gTTS
from googletrans import Translator
translator = Translator()
# This module is imported so that we can 
# play the converted audio
import os
with open('test.txt', 'r') as file:
    mytext_origin = file.read().rstrip() 

# The text that you want to convert to audio
# print("Insert your text:")
# mytext_origin = input()
# mytext_origin = 'Am nevoie de asta în 2 ore de acum înainte. nu licitați dacă nu îl puteți finaliza acum cât mai curând posibil. va rog sa vedeti poza atasata. este o captură de ecran a unui poster. Am nevoie de cineva care să recreeze designul și să-mi trimită fișierul de design în format pdf, ca să îl pot imprima. foarte usor! Am nevoie de asta în 2 ore de acum înainte.'# here you can change the text
mytext = translator.translate(mytext_origin, dest='ro').text  
# Language in which you want to convert
language = 'ro'
print(mytext)
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