# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = input('Введите текст: ')
print(' '.join(filter(lambda my_text: not 'абв' in my_text, my_text.split())))