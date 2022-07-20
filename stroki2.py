# replace(old, new. [count]) - меняет в строке old на new, если вы укажите count

# text = 'ha ha ha ha '
# # print(text[::-1])
# result = text.replace('a', 'i', 2)
# print(result)
# print(text)
# str1 = 'Hello world! My name is John Snow!'
# print(str1.replace('John', 'Sadyr'))

# # strip() - убирает пробельные символы в начале и в конце строки 
# # rstrip, lstrip 
# text = input('Enter the text: ')            
# print(text)
# result = text.strip()                       #убирает пробелы в начале и в конце
# print(result)

# text = '  hello  '
# print(len(text))
# result = text.strip()
# print(result)
# print(len(result))


# startswith(string, [start], [end]) - возращает True, если строка начинается с string, иначе False 

# text = 'Hello world!'
# print(text. startswith('W'))
# print(text. startswith('H'))
# print(text. startswith('h'))
# print(text.startswith('d', -2))

#---------------------------------------------------------------------------------------------------
# print(id('h'))
# print(id('H'))
#---------------------------------------------------------------------------------------------------

# from curses.ascii import isalpha
# isalpha() - проверяет состоит ли наша строка из символов (букв латинского алфавита или кирилицы)



# from curses.ascii import isdigit
# isdigit() - провряет состоит ли наша строка полностью из чисел True 



# from curses.ascii import isalnum
# isnumeric() - проверяет состоит ли нашей строка полностью из чисел 


# text = '777777777'
# print(text.isdigit())
# print(text.isnumeric())
# str.istitle()

# index(values, [status], [end]) - выводит индекс значения values  в нашей строке 

# text = 'Hello world! My name is John!'
# result = text.index('world')                           #index -> обозначает с какого символа начинается строка(слово) 
# print(result)

# rindex -> поиск с конца 

# find(value, [start], [end]) -> делает то же самое что и index. Разница в том что, если value не найден, то возраает -1 
# rfind 

# text = 'Hello'
# print(text.find('y'))

# count('string'[start], [end]) ->  считает количество вхождений string внашу строку 
# text = 'Hello world! I\'m from Earth!'
# result = (text.count('o'))
# print(result)

# swapcase() -> возращает сроку, в которой каждая буква будет иметь противополжный регистр 
# upper(), lower()

# text = 'Hello world, John, SNOW'
# print(text.swapcase())
# print(text.upper())                                  # делает все в строке с большой буквой 
# print(text.lower())                                  #делает все в строке с маленькой буквой


# capitalize() -> переводит первую букву в верхний регистр
# print('hello'.capitalize())
# print(input('Enter your name: ').lower().capitalize())

#istitle ->  переводит символы всех слов в строке в верхний регистр, через пробел

# text = 'john jamia sansa nursultan jerry'
# print(text.istitle())
# print(text.capitalize())

# split(разделитель) -> Дробит строку по разделителю которой находиться в строке. Разделяют строку и возвращает тип данных list 

# from typing import Iterable


# text = 'let me speak from my hearth in English'
# ls = text.split(' ')
# print(len(ls))

# разделитель.join(iterable) -> соеденяет строки, которые находятся в iterable по разделителю 

# sentence = '-_-'.join(ls)
# print(sentence)
# sentence = ' | '.join(ls)
# print(sentence)

'Hello' 
'sentence'

a = 'Hello'
b = 'sentence sentence sentence sentence'
print(a[::-1])            #вывод текста в обратном порядке
print(b[::-1])            #вывод текста в обратном порядке



