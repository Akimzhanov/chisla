"hello world!"
's vami Kani!'
"""
Hello world my name is John Snow
"""
'''
Hellow world
'''

# Строки в pethon  - Набор последовательности символов, которые мы используем для хранения и предоставления текстоой инфомации.

# Индексация в строке 
# name = 'John'
#         # j = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# Срезы  по индиксам 
#  [start: end: <step>]
# str1 = 'birthday'
# print(str1[5:8])
# print(str1[5:])                    #с 5 символа до конца оставшихся символов выводит на терминал
# print(str1[:5])                    # с начало до 5 символа включительно

# text = 'Hello world! My name is John! I\'m King of North!'             #\ обратый слеш для актвации отпределенного знака как символ 
# print(text)
# print(text[:13])            # от начало до 13 символа не включительно 
# print(text[::2])            #от наачало до конца перешагивая по 2 символа 
# print(text[::-1])           #Написание текста в обратном порядке

#Конкатенация строк 
# a = 'Hello'
# b = 'world'
# c = ' '
# result = a + c + b
# print(result)


# Экранирование -при помощи которого можно вставлять символы в строку, которые сложно ввести с клавиатуры 
# \n -> перенос строки 
# \t -> горизонтальная тобуляция 
# \v -> вертикальная тобуляция
# \f -> перевод страцы 
# \r -> возврат указателя 


# name = 'John\nSnow'           #\n переносит строку 
# print(name)
# print(len(name))              #выводит длинну строки 


#Форматирование строк 
# 1. С помощью знака %
# 2. С использованием методо format()
# 3. Интерполяция строк (f-строки)

# %                                                   #форматирует все в строку с помощью %
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello mr/mrs %s %s' %(name, last_name))

# .format                                             # форматирует все с помощью {}
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello mr/mrs {} {}' .format(name, last_name))

# f-строки
# a = input('Enter mr/mrs: ')
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print(f'Hello {a} {last_name} {name}. Welcome to the parthy!' )            # в начале всего ставляем f и в внутри ковычек пишем весь текст, форматируем текст 


# print(dir(str))









