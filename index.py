#Типы данных в притоне:

#1. NoneType -> ничего, пустое
#None#NoneType

#a = None
#print(a)
#2.Boolean -> Правда или ложь (True/False)
#True = 1
#False = 0
#Числовые типы данных :
#          a. integer(int) -> целое число (1,2,3,4,5)
#          b. float() -> числа с правающей точкой (1.2, 10.20, 2.7)
#          c. complex() -> комплексные числа (3+5i/j)

# Списковые типы данных:  
#         a.list(список/массив) -> [1,2,3, True, None ]
#         b.tuple(кортеж) -> (1,2,3, False)
#         c. range(последовательность) -> range(1,5) -> 1,2,3,4
# 5. string(str) строка -> "Hello world"
#         'Hello world'
#John = 'My name is John!'
# 6. set() - множество 
# 7. dict(словари) -> содежит данные в виде ключа: значение -> {1: 'one', 2: 'two'}


###############################################################################################################


#Mutable(Изменяемые типы данных)
# 1.list()
# 2.set()
# 3.dict()

#Immutable(неизменяемые типы данных)
#1. None
#2. bool
#3. int(), float(), complex()
#4.str()
#5.range()
#6.tuple()

print('Hello world, my name is John Snow')

#Стандартный вввод данных
''' Для ввода используется функиця input()
'''

a = input('Введите число:')
print(a)
# type() выводит тип данных
print (type(a))

b = int(input('Введите число номер 2:'))
print(b)
print(type(b))


