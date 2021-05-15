from googletrans import Translator
sen = str(input('Enter the sentences: '))
k = Translator()
lang = str(input('Your Language: '))
convert = str(input('Which Language: '))
data = k.translate(sen, src=lang, dest=convert)
print(data.text)
