import subprocess
import os
# from translate import Translator
from googletrans import Translator
translator = Translator()
# from playsound import playsound

# The text that you want to convert to audio
mytext_origin = 'I am looking for someone knowledgeable in both Tableau and Python'
# translator = Translator(to_lang = "ro")
# mytext = translator.translate(mytext_origin)  
# mytext_origin = 'I am looking for someone knowledgeable in both Tableau and Python'
mytext = translator.translate(mytext_origin, dest='ro').text 
print(mytext)

# set up synthesis input
voice = 'ro+m3'
audio_format = 'mp3'

# generate speech using espeak-ng
output_file = 'output.mp3'
speed = '180'
espeak_cmd = ['espeak', '-v', voice, '-s', speed, '-w', output_file, mytext]

subprocess.run(espeak_cmd)
os.system(output_file)
# play audio using playsound
# playsound(output_file)