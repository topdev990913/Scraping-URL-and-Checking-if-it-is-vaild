import pyttsx3
from googletrans import Translator
translator = Translator()
mytext_origin = 'I am looking for someone knowledgeable in both Tableau and Python'
text = translator.translate(mytext_origin, dest='ro').text 
print(text) 
engine = pyttsx3.init()

engine.setProperty('voice', 'ro-RO')
engine.say(text)
engine.save_to_file(text, 'output1.mp3')
engine.runAndWait()
# Changing the speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # Adjust the rate as per your preference

# Changing the volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.8) 