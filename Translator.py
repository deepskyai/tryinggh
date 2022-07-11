#Translation part
from translate import Translator

translator = Translator(to_lang='ja')
# japanese_message = translator.translate('This is a pen')
# print(japanese_message)

#IO part
with open('exercise.txt', mode='r+') as exercise:
	en_message = exercise.read()
	ja_message = translator.translate(en_message)
	exercise.write(ja_message)