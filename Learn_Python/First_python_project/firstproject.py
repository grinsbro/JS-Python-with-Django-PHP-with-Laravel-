# name = 'Илья'

# print(type(name))

# # type (переменная). Так выводится тип данных
# # Boolean пишется всегда с большой буквы True/False

# # friend = int(input('Введите друга: ')) input() Эта функция дает возможность ввести что-то из консоли и записать это в переменную
# # Чтобы преобразовать в число нужно использовать функцию int()

# friend = input('Введите имя друга: ')

# print("Ваш друг: ", friend)

# Математические операции

# result = 5 + 10
# result2 = 10 - 5
# result3 = 5 * 5
# result4 = 5 / 2
# result5 = 5 // 2 # так получается целочисленное деление
# result6 = 5**2 # Это возведение в степень
# result7 = -142
# result8 = abs(result7) # abs() убирает минус перед числом

# Условные операторы

# num1 = int(input('Введите ваше число: '))

# # usl1 = num1 > 10 and num1 % 2 == 0 # это аналог &&
# # usl2 = num1 % 3 == 0 or num1 > 100 # это аналог ||

# if num1 > 10 and num1 % 2 == 0:
#     print('Число больше 10 и четное')
# elif num1 % 2 != 0:
#     print('Нечетное число')
# elif num1 == 8:
#     print('Число 8')
# else:
#     print('Пока')

# print('Конец программы')

# usl1 = True
# print(not(usl1)) # Данная функция переводит в противоположное значение

# Типа калькулятор

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# action = input('Что вы хотите сделать? (сложить, вычесть, умножить и тд)')

# print('Запускаю калькулятор....')
# print ('...')

# if action == '+':
#     print ('Результат: ', num1 + num2)
# elif action == '*':
#     print ('Результат: ', num1 * num2)
# elif action == '-':
#     print ('Результат: ', num1 - num2)
# elif action == '/':
#     print ('Результат: ', num1 / num2)
# elif action == '**':
#     print ('Результат: ', num1 ** num2)
# else:
#     print('Ошибка')

# print ('Конец программы')

# цикл while

# num1 = 5

# while num1 > 0:
#     num1 -= 1
#     if num1 != 3:
#         print(num1)
#     else:
#         continue # continue пропускает итерацию цикла. Break просто завершает цикл

# print('Конец')

# Цикл for

# str1 = 'Hello'
# for i in str1:
#     print(i)

# range(1,11,2) эта функция перебирает числа. Первый аргумент это начальное число, второй конечное не включительно, а третье это шаг

# len() Это функция, которая показывает длину элемента, который туда передали

# str1 = 'Hello'

# for i in range(len(str1)):
#     print(str1[i])

# Функции

# def print_hello(): # Так определяется функция
#     print('Привет, я функция')

# def sayHello(name):
#     print('Привет, ', name, '!')

# sayHello('Илья')

# def sumNum (a,b):
#     result = a + b
#     return result

# num1 = 50
# num2 = 25

# sumNum(num1,num2)

# Классы, методы и т.д

# class user():
    
#     def __init__(self, name, age, password): #  init это конструктор в питоне

#         self.name = name
#         self.age = age
#         self.password = password

#     def printUser(self):
#         print('Я', self.name, ' Мне', self.age, ' Мой пароль: ', self.password)

# user1 = user('Ilia', 24, 123531)

# user1.printUser() # Так вызываются свойства и методы класса

# print('Мое имя: ', user1.name) # Так вызываются свойства и методы класса

# class dog():
    
#     def __init__(self, name, breed, age, owner):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.owner = owner

# dog1 = dog('Bebrius', 'Pug', 5, 'Ilich')

# print(dog1.breed)

# Строки

# str1 = 'Ilich'

# print(str1[0])

# # Строка - неизменяемый тип данных

# print(str1[0:3]) # Так можно выводить данные из строки с определенного индекса по нужный

# str3 = str1[0:5:2]

# print(str3)

# # методы строк

# print(str1.count('i')) # метод для подсчета количества определенных символов в строке

# print(str1.find('c')) # Показывает индекс нужного символа в строке

# print(str1.rfind('i')) # Показывает индекс нужного символа в строке, но ищет с конца

# print(str1.index('i')) # Также показывает индекс нужного символа в строке

# print(str1.rindex('i')) # Также показывает индекс нужного символа в строке, но ищет с конца

# print(str1.lower()) # переделывает строчку в нижний регистр

# print(str1.upper()) # Переделывает строчку в верхний регистр

# strTest = '1010100011011000111'

# strTest2 = strTest.replace('0', '*') # replace заменяет указанные данные на определенное значение
# print(strTest2)

# Списки

# lst = [1,2,1,3,4,1,5,100,1000,4353,346,2139]

# list = list('Hello') # С помощью этой функции можно разбить строку на массив

# # Списки - изменяемый тип данных

# lst.append(10) # этот метод добавляет данные в конец списка
# print(lst)

# lst.remove(4) # этот метод удаляет определенное значение из списка, но только первое
# print(lst)

# lst.insert(3, 'Hello') # вставляет данные в список по индексу
# print(lst)

# del lst[6] # Удаляет значение по индексу
# print(lst)

# lst.sort() # Сортирует список по возрастанию
# print(lst)
# # Чтобы отсортировать по убыванию в аргументы sort надо написать reverse = true

# str1 = '1 2 3 4 5 6 7 8 9 10'
# lis = str1.split() # Разбивает строку на список
# print(lis)

# Словари, кортежи и множества

# Кортеж
# tup1 = tuple('Hello') # Это кортеж. Иными словами это неизменяемый массив/список
# tup2 = (1,2,4,5,6,7) # так тоже можно создать кортеж

# # Словарь

# dict1 = {'name':'Ilich', "age": 24} # Это словарь. Это то же, что и ассоциативный массив
# # Словари - изменяемый тип данных
# dict2 = dict(name = 'Ilich', age = 24) # Так тоже можно создавать словари

# # Методы словарей

# print(dict2.keys()) # Возвращает ключи словаря
# print(dict2.values()) # Возвращает значения словаря
# print(dict2.items()) # Возвращает элементы разбитые на кортежи
# print(dict2.get('name')) # Возвращает значение нужного ключа
# print(dict2.pop('name')) # Удаляет ключ, который указан, а также возвращает значение ключа
# print(dict2.popitem('name')) # Также удаляет, но уже элемент который указан, и возвращает кортеж ключ->значение

# Множества
# listTest1 = [1,23,45,6,1,234,23,56,45,6,23,56]
# set1 = set(listTest1) # множества это массив  неповторяющихся значений

# set2 = set()
# set2.add('s') # так добавляются элементы в множество
# set2.remove('s') # так удаляются элементы в множество

# froz=frozenset('sdfdsfgs;kjabbljb') # так создается неизменяемое множество

# Работа с файлами в Python

# file1 = open('First_python_project/text.txt') # так можно открыть файл
# test1 = file1.read() # Так можно прочитать содержимое файла
# test1 = file1.readline() # Так можно прочитать определенную строчку файла
# test1 = file1.readlines() # С помощью этого метода можно получить кортеж из содержимого файла
# file1.close() # Так файл закрывается, когда с ним работа закончена

# with open('First_python_project/text.txt') as f: Так тоже можно работать с файлами. Закрывать его, если открыт таким образом не нужно

# Обработка ошибок в Python

# С помощью try, except можно проверять код на ошибки, но если внутри возникнет ошибка, то дальнейший код все равно будет выполняться и выведется код из except
# try:
#     f= open('First_python_project/text.txt', 'r+')
#     f.write('24')
# except Exception as e: # с помощью  Exception as e можно отловить, что именно за ошибка возникла и вывести ее
#     print('Возникла ошибка', e)
# finally: # в finally записывается код, который выполнится в любом случае. Есть ошибка или все прошло без ошибок, он выполнится
#     f.close()
#     print('Файл закрыт')

# print('Конец кода')

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     print('Результат деления ваших чисел: ', num1/num2)
# except ValueError as e: # Так можно отловить, что тип данных введен неправильно
#     print('Возникла какая-то ошибка', e)
# except ZeroDivisionError as e: # Так можно вывести ошибку, что делится на ноль
#     print('На ноль делить нельзя!', e)
# finally:
#     print('Конэц')

# модули и импорт в Python

#import functions # Так импортируются файлы. Но чтобы он импортировался, нужно один раз его запустить и тогда все будет работать здесь 

# functions.sayHello('Илья')
# functions.printAge(25)

# from functions import sayHello # Так можно импортировать определенные функции или переменные из файла

# sayHello('Илья')

# from random import randint # так можно вызвать рандомное число. random это встроенный модуль, который может присылать рандомные значения
# a1 = randint(10, 20)
# print(a1)

# lambda функции в Python

# func1 = lambda x,y : x+y # Так можно записать простую функцию, которая выполняет математическое действие

# # Map
# list1 = ['123','23','1', '15', '42', '143']
# listRes = list(map(int, list1)) # с помощью map можно применять какую-то функцию к спискам

# listDollars = [23, 35, 67,78,90]
# listrub = list(map(lambda x: x * 90, listDollars))

# # Filter

# listStud = ["Илья", "Сэм", "Магомед", "Павел", "Сэд", "Рома"] 
# listFilter = list(filter(lambda name : len(name) > 3, listStud )) # С помощью фильтра можно задать определенное условие по фильтрации (очевидно)

# # zip

# listC = [1,2,3,4]
# strC = 'ABCD'
# tupleC = (True, False, True, False)
# res = list(zip(listC, strC, tupleC)) # С помощью zip можно разбить разные данные по кортежам по индексам


# ООП в питоне

# class Cat():
    
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def printInfo(self):
#         print('Меня зовут', self.name)
#         print('Мне', self.age)
#         print('Я цвета: ', self.color)
    
#     def May(self):
#         print('MYYYYYYYYA', self.name, 'meows')


# cat1 = Cat('Vasiliy', 18, 'Black')
# cat1.printInfo()
# cat1.May()
# cat2 = Cat('Belyash', 3, 'White')
# cat2.printInfo()
# cat2.May()
# cat3 = Cat('Musya', 7, 'Amber')
# cat3.printInfo()
# cat3.May()

# class User():

#     def __init__(self,name,age,salary):
#         self.__name = name # двойное нижнее подчеркивание это то же, что и private, то есть переменная становится неизменяемой
#         self.__age = age
#         self.__salary = salary

#     def printInfo(self):
#         print(self.__name, 'получает', self.__salary)

#     def getSalary(self): # это геттер
#         return self.__salary
    
#     def setSalary(self, salary): # это сеттер
#         self.__salary = salary
#         print('зарплата изменена')

#     # геттер и сеттер можно записать вот так
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name = name

# user1 = User('Иван', 24, 120000)
# print(user1.name)

# магические методы - это возможность переопределять какие-то действия для объектов

# class Dog():
    
#     def __init__(self, name, age, sila):
#         self.__name = name
#         self.__age = age
#         self.__sila = sila
    
#     def __str__(self): # Этот метод дает возможность определить как объект будет выглядеть в виде строки
#         return f'Это собака по имени: {self.__name}'
    
#     def __eq__(self, dog): # Этот метод позволяет сравнивать определенные значения у объектов
#         if self.__age == dog.__age:
#             return True
#         return False
    
#     def __gt__ (self, dog): # Этот метод переопределяет сравнение больше/меньше
#         if self.__sila > dog.__sila:
#             return True
#         return False

#     def __add__(self, dog): # Этот метод переопределяет сложение
#         return self.__age + dog.__age

# dog1 = Dog('Barsik', 12, 190)
# dog2 = Dog('Shelushayka', 3, 1999)

# Статические, обычные и методы

# class Voin():

#     __maxSila = 1000
#     __listVoins = []

#     def __init__(self, name, hp, sila):
#         self.__name = name
#         self.__hp = hp

#         if sila >= Voin.__maxSila:
#             self.__sila = Voin.__maxSila
#         else:
#             self.__sila = sila
        
#         Voin.__listVoins.append(self)
    
#     def printInfo(self):
#         return f'Это воин по имени {self.__name}, его сила: {self.__sila}'
    
#     @classmethod # этот метод имеет отношение только к классу, но не к объекту, который был создан на его основе
#     def getMaxSila(cls):
#         return cls.__maxSila

#     @staticmethod # метод, который можно вызывать у объекта и класса, но он не имеет представления о переменных внутри
#     def helloVoin():
#         print('Привит воины')

#     @classmethod
#     def getLst(cls):
#         lst = cls.__listVoins
#         for voin in lst:
#             print(voin.printInfo())


# voin1 = Voin('Спартак', 999, 300)
# voin2 = Voin('Август', 999, 2500)
# # print(voin1.printInfo())
# # print(voin2.printInfo())

# # Voin.helloVoin()
# # voin1.helloVoin()
# Voin.getLst()


# val = int(input('Введите количество звездочек: '))
# mult = ''

# while len(mult) < val:
#     mult += '*'
#     print(mult)

# val = int(input('Введите максимальное значение: '))

# for i in range(0,val+1):
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

# num = int(input('Введите число: '))
# count = 0
# for x in range(num+1):
#     if x % 3 == 0:
#         count += x
#     if x % 5 == 0:
#         count += x
#     else:
#         continue
# print(count)

# firstList = [1,2,3,4,5]
# secondList = [11,12,13,14,15]
# oddList = []
# evenList = []
# for i in firstList:
#     if i % 2 != 0:
#         oddList.append(i)
#     else:
#         evenList.append(i)
# for i in secondList:
#     if i % 2 != 0:
#         oddList.append(i)
#     else:
#         evenList.append(i)
# print(oddList)
# print(evenList)

# curentHand = [2,3,4,10,'Q',5]
# weight = 0

# for i in curentHand:
#     if i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
#         weight += 1
#     elif i == 7 or i == 8 or i == 9:
#         weight += 0
#     else:
#         weight -= 1

# print(weight)

# from functools import wraps

# def logDecorator(func):
#     @wraps(func)
#     def wrap():
#         print(f'Calling func {func.__name__}')
#         func()
#         print(f'Func {func.__name__} finished its work')
#     return wrap

# @logDecorator
# def hello():
#     print('Hello world!')

# help(hello)

# def getreply(number):
#     if number % 5 == 0 and number % 3 == 0:
#         return 'FizzBuzz'
#     elif number % 3 == 0:
#         return 'Fizz'
#     elif number % 5 == 0:
#         return 'Buzz'
#     else:
    
#         return ''
    

# class Character():
    
#     max_speed = 100
#     dead_health = 0

#     def __init__(self, race, damage=10, armor=20):
#         self.race = race
#         self.damage = damage
#         self.armor = armor
#         self.health = 100
    
#     def hit(self, damage):
#         self.health -= damage

#     def is_dead(self):
#         return self.health == Character.dead_health

# unit = Character('Elf', 50, 100)

# unit.hit(20)
# print(unit.health)
# unit.hit(80)
# print(unit.is_dead())


# class Character():

#     MAX_SPEED = 100 # Так записывают константы. Несмотря на то, что ее можно переписать, есть неписанное правило, что если переменная записана капсом, то ее лучше не перезаписывать

#     def __init__(self, race, damage = 10):
#         self.__race = race # Это приватный атрибут(private), то есть его нельзя нигде использовать, кроме класса, где он был объявлен
#         self.damage = damage
#         self._health = 100
#         self._current_speed = 20

#     def hit(self,damage):
#         self._health -= damage # Это защищенный атрибут(protected), то есть его можно использовать в классах наследниках

#     @property # Это декоратор для прописывания геттера
#     def health(self):
#         return self._health
#     @property
#     def race(self):
#         return self.__race
    
#     @property
#     def current_speed(self):
#         return self._current_speed
    
#     @current_speed.setter # Так прописывается сеттер. Название свойства всегда должно быть таким же как атрибут
#     def current_speed(self, speed):
#         if speed < 0:
#             self._current_speed = 0
#         elif speed > 100:
#             self._current_speed = 100
#         else:
#             self._current_speed = speed
    

# ch1 = Character('Elf')

# class StaticTest():
#     x = 1

# t1 = StaticTest()

# t1.x = 2

# StaticTest.x = 3
# print(f'Via instance: {t1.x} ')

# print(f'Via class: {StaticTest.x}')

# class Date():

#     def __init__(self, month, day, year):
#         self.month = month
#         self.day = day
#         self.year = year

#     def display(self):
#         return f'{self.day}/{self.month}/{self.year}'
    
#     @classmethod
#     def millenium_c(cls, month, day):
#         return cls(month,day, 2000)
    
#     @staticmethod
#     def millenium_s(month, day):
#         return Date(month, day, 2000)
    
# d1 = Date.millenium_c(6,9)
# d2 = Date.millenium_s(6,9)

# print(d1.display())
# print(d2.display())

# class DateTime(Date):
#     def display(self):
#         return f'{self.day}/{self.month}/{self.year} - 00:00:00 PM'
    
# dt1 = DateTime(10,10,1990)
# dt2 = DateTime.millenium_s(10,10)

# print(isinstance(dt1, DateTime))
# print(isinstance(dt2, DateTime))

# print(dt1.display())
# print(dt2.display())

# class StrConverter():

#     @staticmethod
#     def to_str(bytes_or_str):
#         if isinstance(bytes_or_str, bytes):
#             value = bytes_or_str.decode('utf-8')
#         else:
#             value = bytes_or_str
#             return value
        
#     @staticmethod
#     def to_bytes(bytes_or_str):
#         if isinstance(bytes_or_str, str):
#             value = bytes_or_str.encode('utf-8')
#         else:
#             value = bytes_or_str
#             return value

# class Shape():

#     def __init__(self):
#         print('Shape created')

#     def draw(self):
#         print('Drawing a shape')

#     def area(self):
#         print('Calc area')
    
#     def perimeter(self):
#         print('Calc perimeter')

# class Rectangle(Shape):

#     def __init__(self, width, height):
#         Shape.__init__(self)

#         self.width = width
#         self.height = height

#         print('Rectangle created')

#         Shape.area(self)

#     def area(self):
#         return self.width * self.height


#     def perimeter(self):
#         return 2*(self.width+self.height)

#     def draw(self):
#         print('Drawing rectangle')

# rectangle = Rectangle(10,15)
# import math
# class Triangle(Shape):

#     def __init__(self, a, b, c):
#         super().__init__()

#         self.a = a
#         self.b = b
#         self.c = c

#         print('Triangle created')

#     def draw(self):
#         print(f'Drawing triangle with sides {self.a}, {self.b}, {self.c}')

#     def area(self):
#         s = (self.a + self.b + self.c)/2
#         return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
#     def perimeter(self):
#         return self.a + self.b + self.c
    
# triangle = Triangle(10,10,10)

# for shape in [rectangle, triangle]:
#     shape.draw()

# class Animal():
#     def die(self):
#         print('bye bye')
#         self.health = 0

# class Carnivour():
#     def hunt(self):
#         print('eating')
#         self.satiety = 100

# class Dog(Animal, Carnivour):
#     def bark(self):
#         print('woof-woof')

# dog1 = Dog()

# dog1.bark()
# dog1.hunt()
# dog1.die()

# class Animal():
#     def set_health(self,health):
#         print('set in animal')

# class Carnivour(Animal):
#     def set_health(self,health):
#         super().set_health(health)

#         print('set in carnivour')

# class Mammal(Animal):
#     def set_health(self, health):
#         super().set_health(health)

#         print('set in mammal')

# class Dog(Mammal, Carnivour):
#     def set_health(self, health):
#         super().set_health(health)

#         print('set in dog')

# dog1 = Dog()

# dog1.set_health(10)

# МиксИны

# class Vehicle():

#     def __init__(self, position):
#         self.position = position
    
#     def travel (self,destination):
#         route = calculate_route(source=self.position, to = destination) # type: ignore
#         self.move_along(route)

#     def calculate_route(self,source, to):
#         return 0
    
#     def move_along(self,route):
#         print('moving')

# class Airplane(Vehicle):
#     pass

# class RadioMixin():

#     def __init__(self):
#         self.radio = Radio()

#     def turn_on(self,station):
#         self.radio.set_station(station)
#         self.radio.play()

# class Radio():
#     def set_station(self,station):
#         self.station = station

#     def play(self):
#         print(f'playing {self.station}')

# class Car(Vehicle, RadioMixin):

#     def __init__(self):
#         Vehicle.__init__(self, (10,20))
#         RadioMixin.__init__(self)

# car = Car()
# car.turn_on("Moscow FM")

# from abc import ABC
# from abc import abstractmethod
# from math import sqrt

# class Shape(ABC):

#     def __init__(self):
#         super().__init__()

#     @abstractmethod # таким образом можно прописывать, что метод является абстрактным
#     def draw(self):
#         pass    

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         print('calc perimeter')

#     def drag(self):
#         print('Basic dragging func')

# class Triangle(Shape):

#     def __init__(self,a,b,c):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.c = c

#     def draw(self):
#         print(f'Drawing triangle with sides {self.a}, {self.b}, {self.c}')

#     def area(self):
#         s = (self.a + self.b + self.c)/2
#         return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
#     def perimeter(self):
#         super().perimeter()
#         return self.a+self.b+self.c

#     def drag(self):
#         super().drag()
#         print('Additional actions')

# t1 = Triangle(10,10,10)
# print(t1.perimeter())
# print(t1.drag())

#ДЗ по классам

# class Name:

#     def __init__(self, first_name, last_name):
#         self.firstname = first_name.capitalize()
#         self.secondname = last_name.capitalize()
#         self.fullname = f'{self.firstname} {self.secondname}'
#         self.initials = f'{self.firstname[:1]}.{self.secondname[:1]}'

# a1 = Name('john', 'SMITH')

# print(a1.firstname)
# print(a1.secondname)
# print(a1.fullname)
# print(a1.initials)

# class Calculator:

#     def add(self, a,b):
#         return a + b
    
#     def substract(self, a,b):
#         return a - b
    
#     def multiply(self, a,b):
#         return a * b
    
#     def divide(self, a,b):
#         return a / b

# calc = Calculator()

# print(calc.add(10,5))
# print(calc.substract(10,5))
# print(calc.multiply(10,5))
# print(calc.divide(10,5))

# class Employee:

#     def __init__(self, firstname, secondname, salary):
#         self.first_name = firstname
#         self.second_name = secondname
#         self.salary = salary

#     @classmethod
#     def from_string(cls, str):
#         first_name, second_name, salary = str.split('-')
#         return cls(first_name, second_name, salary)

# emp1 = Employee('Mary', 'Sue', 60000)
# emp2 = Employee.from_string('John-Smith-55000')

# print(emp1.first_name)
# print(emp1.salary)
# print(emp2.first_name)
# print(emp2.salary)


# class Pizza():
    
#     orderCount = 0

#     def __init__(self, ingredients):
#         self.ingridients = ingredients
#         Pizza.orderCount += 1
#         self.order_number = Pizza.orderCount

#     @classmethod
#     def garden_feast (cls):
#         return cls(['spinach', 'olives', 'mushroom'])
    
#     @classmethod
#     def meat_festival (cls):
#         return cls(['beef', 'meatball', 'bacon'])
    
#     @classmethod
#     def hawaiian (cls):
#         return cls(['ham', 'pineapple'])

# p1 = Pizza(['bacon','parmesan', 'ham'])
# p2 = Pizza.garden_feast()
# p3 = Pizza.hawaiian()
# p4 = Pizza(['beef','olives'])

# print(Pizza.orderCount)
# print(p1.order_number)
# print(p2.order_number)
# print(p3.order_number)
# print(p4.order_number)

# from math import pi
# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return (self.radius**2) * math.pi

#     def get_perimeter(self):
#         return 2 * self.radius * math.pi
    
# circ = Circle(10)

# area = circ.get_area()
# perimeter = circ.get_perimeter()

# print(area)
# print(perimeter)

# prices = {'Strawberries': 1.50, 'Banana': 0.50, 'Mango': 2.50, 'Blueberries': 1.00, 'Raspberries': 1.00, 'Apples': 1.75, 'Pineapple': 3.50}

# class Beverage:

#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.cost = sum([prices[fruit] for fruit in self.ingredients])
#         self.price = self.cost * 2.5

#     def get_cost(self):
#         return f'${self.cost:.2f}'
    
#     def get_price(self):
#         return f'${self.price:.2f}'
    
#     def get_name(self):
#         lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
#         return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'

# s1 = Beverage(['Banana'])

# print(s1.ingredients)
# print(s1.get_cost())
# print(s1.get_name())
# print(s1.get_price())

# s2 = Beverage(['Banana', 'Strawberries', 'Blueberries'])

# print(s2.ingredients)
# print(s2.get_cost())
# print(s2.get_name())
# print(s2.get_price())

# from progressbar import ProgressBar
# import time

# bar = ProgressBar(maxval=10)
# bar.start()

# for i in range(1,11):
#     bar.update(i)
#     time.sleep(1)

# bar.finish()

# отладка (debugging)
# import pdb

# x = 1
# y = 2

# pdb.set_trace() # это метод, который делает так, чтобы исполнение скрипта остановилось тут и не выполнялось дальше. Это нужно, чтобы отловить ошибки на каком-то отрезке
# # При исполнении появляется строка, куда можно записать команды или значение переменных. "с" это continue, продолжает выполнение до следующей точки. "next" это следующая инструкция, и если есть функция, то зайдет внутрь этой функции
# # Также есть команда "step", которая также идет к следующей инструкции, но не заходит внутрь функции. Чтобы остановить отладчик нужно написать "q"
# z = 3
# x += 1

# pdb.set_trace()

# print('Finish')

# Stack (итерируемые объекты)

# class MyStack:

#     def __init__(self):
#         self.array = []

#     def push(self, item):
#         self.array.append(item)

#     def pop(self):
#         popped_item = self.array.pop()
#         return popped_item
    
#     def peek(self):
#         return self.__current()
    
#     def __current(self):
#         return self.array[self.count()-1]
    
#     def count(self):
#         return len(self.array)
    
#     def __iter__(self):
#         self.index = self.count()-1
#         return self
    
#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration()
#         result = self.array[self.index]
#         self.index -= 1
#         return result
    
# stack = MyStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())
# print(stack.peek())
# print(stack.count())
# stack.push(4)
# stack.push(5)
# stack.push(6)

# for i in stack:
#     print(i)

# Дата и время

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# d1 = date(2025, 3, 20) # Так задается дата
# print(d1)
# print(d1.year)
# print(d1.month)
# print(d1.day)
# print(date.today())
# print(date.max)
# print(date.min)

# t1 = time(15, 0,0) # Так задается время
# print(t1)
# print(t1.hour)
# print(t1.minute)
# print(t1.second)
# print(time.max)
# print(time.min)

# dt = datetime(2025,3,20,15,2,0)
# print(dt)
# print(datetime.now())

# dt = datetime.strptime('30/08/2024', '%d/%m/%Y') # Так можно парсить из строки в формат времени
# print(dt)

# dt = datetime.strptime('29/03/2024 10:40', '%d/%m/%Y %H:%M')
# print(dt)

# dt = datetime.strptime('06-28-2020', '%m-%d-%Y')
# print(dt)

import locale
# locale.setlocale(locale.LC_ALL, "") # Таким образом устанавливается локаль, чтобы названия были на

# now = datetime.now()
# print(now.strftime('%Y-%m-%d (%a)'))
# print(now.strftime('%Y-%b-%d число (%A)'))

# delta1 = timedelta(days=3, hours=2, minutes=10)

# my_birthday = date(2000,12,22)
# delta = date.today() - my_birthday
# print(type(delta))

# my_age = int(delta.days/365)
# print(my_age)

# wife_birthday = date(2001,7,24)
# am_i_older = my_birthday < wife_birthday
# print(am_i_older)

# # Singleton
# class Character: 

#     # Так прописывается singleton (у класса может быть только один объект)
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self):
#         self.race = 'Elf'

# c = Character()
# print(c.race)
# d = Character()
# d.race = 'Ork'
# print(c.race)
# print(d.race)

# Консервирование (Pickling)

# class Character:

#     def __init__(self, race, armor, damage = 10):
#         self.race = race
#         self.damage = damage
#         self.armor = armor
#         self.health = 100
    
#     def hit(self,damage):
#         self.health -= damage

#     def is_dead(self):
#         return self.health == 0
    
#     def __getstate__(self): # Здесь можно прописывать, что именно будет записываться в файл в процессе консервирования
#         pass
    
#     def __setstate__(self, state): # Тут прописывается, какой объект возвращается в процессе расконсервирования. Если какого-то атрибута нет, то он заменяется значением по умолчанию
#         self.race = state.get('race', 'Elf')
#         self.damage = state.get('damage', 10)
#         self.armor = state.get('armor', 20)
#         self.health = state.get('health', 100)

# c = Character('Elf', 20)
# c.hit(10)
# print(c.health)

# import pickle

# with open(r'D:\Games\game_state.bin', 'w+b') as f:
#     pickle.dump(c, f)

# c = None
# print(c)
# with open(r'D:\Games\game_state.bin', 'rb') as f:
#     c = pickle.load(f)

# print(c.health)
# print(c.__dict__)

# __str__, __repr__, eq, ne, eval

# from datetime import datetime

# dt = datetime.now()

# print(repr(dt)) # repr выводит описание объекта и его состояние. Например, можно использовать repr, чтобы получить то, как выглядит объект и исполнить его функцией eval
# print(dt)

# class Character:

#     def __init__(self, race, damage=100):
#         self.race = race
#         self.damage = damage

#     def __repr__(self):
#         return f'Character("{self.race}", {self.damage})'
    
#     def __str__(self):
#         return f'{self.race} with damage = {self.damage}'
    
#     def __eq__(self, value): # Так прописывается сравнение, чтобы оно было не ссылочным, а глубоким
#         if isinstance(value, Character):
#             return self.race == value.race and self.damage == value.damage
#         return False
# c1 = Character('Elf')

# d1 = eval(repr(c1))
# print(type(d1))

# print(c1 == d1)

# Поверхностное копирование и глубокое

# list1 = [1,2,3,[4,5,6]]

# copied_list = list1.copy()

# copied_list[3].append(7)

# # print(list1)
# # print(copied_list)

# list1.append(8)
# # print(list1)
# # print(copied_list)

import copy # этот модуль позволяет делать глубокую копию

# shallow_copy = copy.copy(list1)
# shallow_copy[3].append(8)
# # print(list1)
# # print(shallow_copy)

# deep_copy = copy.deepcopy(list1) # Так делается глубокое копирование
# deep_copy[3].append(9)

# print(list1)
# print(deep_copy)

# class Point():

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Point({self.x}, {self.y})'
    
# a = Point(1,2)
# b = copy.copy(a)

# a.x = 3

# print(a.x)
# print(b.x)

# class Line():

#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2

#     def __copy__(self): # Так работает неглубокое копирование по умолчанию
#         cls = self.__class__
#         result = cls.__new__(cls)
#         result.__dict__.update(self.__dict__)
#         return result
    
#     def __deepcopy__(self, memo): # Так работает глубокое копирование по умолчанию
#         cls = self.__class__
#         result = cls.__new__(cls)
#         memo[id(self)] = result

#         for k, v in self.__dict__.items():
#             setattr(result, k, copy.deepcopy(v, memo))

#         return result
# Это выявит проблему, что если класс является составным другого класса, то копия будет делаться поверхностно
# l1 = Line(a,b)
# l2 = copy.copy(l1)

# print(l1.p1)
# print(l2.p1)

# l1.p1.x = 4

# print(l1.p1)
# print(l2.p1)

# Чтобы скопировать глубоко, даже если класс является состаным другого класса, то нужно использовать следующее:

# l1 = Line(a,b)
# l2 = copy.deepcopy(l1)

# print(l1.p1)
# print(l2.p1)

# l1.p1.x = 6

# print(l1.p1)
# print(l2.p1)

# Enum перечисления
# Enum нужен, когда есть несколько связанных по смыслу констант и нужно провожить например какие-то вычисления с ними или как-то взаимодействовать. В таком случае создается класс, который наследуется от Enum, IntEnum или IntFlag и можно так взаимодействовать

from enum import Enum

# class TrafficLight(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3

# print(TrafficLight.RED)

# print(TrafficLight.RED.name)
# print(TrafficLight.RED.value)

# for c in TrafficLight:
#     print(c)

# TrafficLight(1)

# print(TrafficLight.RED == TrafficLight.RED)
# print(TrafficLight.RED == TrafficLight.GREEN)

# from enum import IntEnum

# class Priority(IntEnum):
#     LOW = 1
#     NORMAL = 2
#     HIGH = 3

# print(Priority.LOW < Priority.NORMAL)

# from enum import IntFlag

# class Color(IntFlag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4

# combination = Color.RED | Color.GREEN

# Color.RED in combination

# class Planet(Enum):
#     MERCURY = (3.303e+23, 2.4397e6)
#     EARTH = (5.976e+24, 6.37814e6)
#     JUPITER = (1.9e+27, 7.1492e7)

#     def __init__(self, mass, radius):
#         self.mass = mass
#         self.radius = radius

#     @property
#     def surface_gravity(self):
#         G = 6.67300E-11
#         return G*self.mass/ (self.radius * self.radius)
    
# print(Planet.EARTH.surface_gravity)

# Работа с JSON

import json

# class Tournament():

#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     @classmethod
#     def from_json(cls, json_data):
#         return cls(**json_data)

# tournaments = {
#     "Aeroflot Open": 2010,
#     "FIDE World Cup": 2018,
#     "FIDE Grand Prix": 2016
# }

# методы dump и dumps. Первый сохраняет данные на диске, а второй возвращает JSON формат

# Это сериализация (приведение объекта в какой-то формат)
# json_data = json.dumps(tournaments, indent = 2) # индент это отступы
# print(json_data)

# Это десериализация
# loaded = json.loads(json_data)
# print(type(loaded))
# print(loaded)

# t1 = Tournament("Aeroflot Open", 2010) # Объекты на основе классов не являются сериализуемыми
# json_data = json.dumps(t1)

# Сериализуемые объекты:
# Словари (dict)
# Списки и кортежи (list, tuples)
# Строки (str)
# Числа, дробные (int, float)
# Булевые значения (boolean)
# None

# Чтобы сделать сериализуемым объект на основе класса
# json_data = json.dumps(t1.__dict__) # Чтобы можно было привести в JSON формат объект на основе класса, то нужно вызвать у объекта метод __dict__
# print(json_data)

# t = Tournament(**json.loads(json_data)) # Таким образом он преобразуется обратно
# print(f'name = {t.name}, year = {t.year}')

# Усложнение

# class Chessplayer():
    
#     def __init__(self, tournaments):
#         self.tournaments = tournaments

#     @classmethod
#     def from_json(cls, json_data):
#         tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
#         return cls(tournaments)
    
# t1 = Tournament("Aeroflot Open", 2010)
# t2 = Tournament("FIDE World Cup", 2018)
# t3 = Tournament("FIDE Grand Prix", 2016)

# p1 = Chessplayer([t1,t2,t3])

# json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent= 4, sort_keys=True) # Если в объекта класса есть какая-то вложенность других классов, то нужно прописывать так, чтобы даннеы можно было сериализовать
# print(type(json_data))
# print(json_data)


# decoded_player = Chessplayer.from_json(json.loads(json_data))
# print(decoded_player)
# print(decoded_player.tournaments)

# decoded_player = Chessplayer(**json.loads(json_data))
# print(decoded_player)

# player_tournaments = decoded_player.tournaments[0]
# print(type(player_tournaments))

# print(player_tournaments)

# with open('player.json', "w") as file:
#     json.dump(p1, file, default=lambda obj:obj.__dict__)

# with open('player.json', "r") as read_file:
#     data = json.load(read_file)

# print(data)

# decoded_player2 = Chessplayer.from_json(data)
# print(decoded_player2)
# print(decoded_player2.tournaments)

# Генераторы

import random

# def randoms(min, max, n):
#     return [random.randint(min,max) for _ in range(n)]

# for r in randoms(10,30,5):
#     print(r)

# def randoms(min, max, n):
#     for i in range(n):
#         yield random.randint(min, max) # yield - ключевое слово, которое вызывает генератор

# for r in randoms(10,30,5):
#     print(r)

# rand_sequence = randoms(1,10,10)
# print(type(rand_sequence))

# def randoms(min, max, n):
#     for i in range(n): # Можно также прописывать While True, например, когда неизвестно, сколько чисел нужно будет сгенерировать
#         yield random.randint(min, max)

# import itertools

# rand_sequence = randoms(1,10,10)
# five_taken = list(itertools.islice(rand_sequence, 5))
# print(five_taken)

# def read_line_by_line(file):
#     ""Lazy Function (generator) to read a file line by line.""
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         yield line

# Модуль iterltools

# Все генераторы являются итераторами, но не все итераторы - генераторы. Различие в ключевом слове yield

# Итератор э то объект, который используется для итерации по итерируемому объекту, используя next() dunder-метод
# Любой объект итератор итерируем, но не любой итерируемый объект является объектом итератором.
# Например, list итерируем, но сам по себе итератором не является. Чтобы получить итератор из итерируемого объекта, надо воспользоватьсяметодом iter(), который возвращает объект итератор

# iterable = [1,2,3]

# iterrator = iter(iterable) # Будет вызван метод __iter__()
# print(type(iterrator))

# print(next(iterrator)) # Будет вызван метод __next__()
# print(next(iterrator))
# print(next(iterrator))

import itertools as it

# Бесконечные итераторы

# even_numbers = [x for x in range(10) if x % 2 == 0] # Это способ, который расходует больше памяти
# print(even_numbers)

# even_numbers = it.count(0,2) # Здесь мы создаем итератор, а потом уже в следующей строке пишем, сколько нам нужно чисел. То есть память не занимается сразу всем, а лишь тогда, когда надо и сколько нвдо
# print(list(next(even_numbers) for _ in range(5)))

# def print_iterable(iterable, end = None):
#     for x in iterable:
#         if end:
#             print(x, end=end)
#         else:
#             print(x)
# ones = it.repeat(1,5)
# print_iterable(ones, ' ')

# pos_neg_ones = it.cycle([1,-1])
# print(list(next(pos_neg_ones) for _ in range(10)))

# letters = it.cycle(['A','B', 'C'])
# print(list(next(letters) for _ in range(10)))

# print(list(it.accumulate([1,2,3,4,5])))

# print(list(it.accumulate(['A', 'B', 'C'])))

# print(list(it.accumulate([3,1,4,2,7,3,8,5,9], max)))

# print(list(it.chain('ABC', 'DEF')))

# print(list(it.chain.from_iterable('ABC', 'DEF')))

# print(list(it.dropwhile(lambda x: x<3, [1,2,3,4,5])))

# print(list(it.takewhile(lambda x: x<3, [1,2,3,4,5])))

# print(list(it.filterfalse(lambda x: x%2==0, range(10))))

# names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri', 'Kramnik']
# ratings = [2842, 2822, 2801, 2797, 2780]

# # for name, rating in zip(names, ratings):
# #     print(f'{name}: {rating}')

# players = dict(it.zip_longest(names, ratings))

# print(players)

# for key, grp in it.groupby([1,1,1,2,2,2,3,3]):
#     print('{}: {}'.format(key, list(grp)))

# even_numbers = it.count(0,2)
# print([x for x in range(20) if x%2==0])

# print(list(it.islice(even_numbers, 2,10,2)))

# pin = [7,5,2,8]

# print(list(it.permutations(pin)))

# ranks = ['6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
# suits = ['H', 'D', 'C', 'S']

# lst = list(it.product(ranks,suits))
# print(lst)
# print(list(it.combinations(lst,2)))

# Интроспекция

# print(issubclass.__doc__)

# class Shape:
#     pass

# class Circle(Shape):
    
#     def __init__(self,radius):
#         self.radius = radius

# circle = Circle(10)

# print(issubclass(Circle, Shape))

# print(isinstance(circle, Circle))
# print(isinstance(circle, Shape))

# print(isinstance(12, int))
# print(isinstance('str', str))

# print(isinstance("hi", float))

# print(callable(circle)) # Тут можно получить True, если у класса, инстанцией которого является прописан __call__()
# print(callable(print))

# if hasattr(circle, 'radius'):
#     print(getattr(circle, 'radius'))
#     setattr(circle, 'radius', 20)
#     print(getattr(circle, 'radius'))

# print(dir(circle)) # Так можно посмотреть атрибуты

# print(circle.__dict__)

# print(__name__)

# Модуль requests

import requests

# response = requests.get("https://engineerspock.com/")

# print(type(response))

# response.status_code

# if response:
#     print('Works')

from requests import HTTPError

# for url in ["https://engineerspock.com/", "https://engineerspock.com/inexistent"]:
#     try:
#         response = requests.get(url)

#         response.raise_for_status()
#     except HTTPError as http_error:
#         print(f'Error: {http_error}')
#     except Exception as err:
#         print(f'Unknown errror: {err}')
#     else:
#         print(f'Connected successfully')

# response2 = requests.get('https://api.github.com')

# data = response2.json()
# print(data)

# blog_response = requests.get('https://www.engineerspock.com/')
# github_response = requests.get('https://api.github.com')

# print(blog_response.headers, end='\n')
# print('')
# print(github_response.headers, end='\n')

# placeholder_response = requests.get('https://jsonplaceholder.typicode.com/comments', params = b'postId-1')
# print(placeholder_response.text)

# type hints
# from typing import Optional, Union, Any, List, Tuple, Dict, Iterable

# class Character:
    
#     def __init__(self, armor: int, power: int): # при объявлении аргумента, можно указывать через двоеточие тип данных, который ожидается
#         self.power = power
#         self.armor = armor
#         self.health = 100
        
#     def hit(self, damage: int):
#         self.health -= damage
        
#     def is_alive(self) -> bool: # Так прописывается для функции, результат какого тип ожидается
#         return self.health > 0
    
    
# c1 = Character(10, 20)

# amount: int
# amount = 10

# prince: Optional[int] # Так можно указать, что данные могут быть и числом, и None
# price = 10
# price = None

# attack: Any = 1 # Так можно указывать, что можно передавать любой тип данных в переменную. Но нужно использовать, только если в других переменных указывается тип данных, в противном случае это бессмысленно
# attack = 'Hi'

# length: Union(int, float) # Так можно объединять и указывать, что в переменную могут быть записаны как числа,  так и дробные

# quotes: list # Так можно указать, что эта переменная это список

# quotes: List[int] # Так можно прописать, что в этот список могут быть записаны только числа

# player: Tuple[str, int] # Так прописывается, что в кортеже будет использоваться опеределенный тип данных

# changes_in_rating: Tuple[int, ...] # Так прописывается, что в кортеже будут разные данные одного типа

# chess_player: Dict[str, int] # Так прописывается, что в словаре будут только данные вида строка:число

# def random_stream(min_val: int, max_val: int) -> Iterable[int]: # Так прописывается, что возврвщаться будет итерируемый объект
#     while True:
#         yield random.randint(min_val, max_val)
    

# Walrus оператор (:=)

# print(walrus := True) # так можно сократить количество кода, чтобы не объявлять переменную, а потом принтовать ее. Можно сразу так написать

# for i in range(rows := int(input('Введите количество строк'))):
#     print('*' * (i+1))

# Позиционные аргументы

