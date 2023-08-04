from googletrans import Translator
translator = Translator()
text = "Hello, how are you?"
translated = translator.translate(text, dest='ro')
print(translated.text)