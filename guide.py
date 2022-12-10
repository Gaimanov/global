"""
Характеристика Python - интерпретируемый, мультипарадигруемый язык програмирования со строгой динамической типизацией.
Строгая динамическа типизация - одна переменная в разные моменты времени может иметь разные типы данных(строгая - нет автоматической конверсии типов при каких-то операциях).
Преимущества и недостатки - не очень быстрый(сначала компилирует код в байт-код и потом его интерпритирует), множество библиотек, широкое комюнити
Типы данных - Изменяемые и неизменяемые(При работе с неизменяемыми создается новый объект в памяти). Изменяемые - list,
set, dict. Подтипы: упорядоченные (списки, кортежи, строки и словари),неупорядоченные (множества).
Ключем в словаре может быть любой неизменяемый объект, либо объект у которого реализован магический метод __hash__
Функция - переиспользуемый участок кода, в котором можно параметризировать какие-то значения.
Замыкание -
Распаковка параметров - * и **. * - собираем в кортеж, ** - в dict
Списковое включение(list comp) - Списковое включение создает новый list, применяя выражение к каждому элементу итерируемого.
Наиболее простой формой является: [ <expression> for <element> in <iterable> ]
ООП - методология программирования, основанная на представлении программы в виде совокупности взаимодействующих объектов,
каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования
    Принципы ООП
    Инкапсуляция
    Все объекты в Python инкапсулируют внутри себя данные и методы работы с ними, предоставляя публичные интерфейсы для
    взаимодействия.
    Атрибут может быть protected()
    Наследование
    Язык программирования Python реализует как стандартное одиночное наследование, так и множественное:
        class Mammal():
        className = 'Mammal'

        class Dog(Mammal):
        species = 'Canis lupus'

        class Horse():
        isHorse = True

        class Donkey():
        isDonkey = True
        class Mule(Horse, Donkey):
        mule = Mule()
        mule.isHorse # True
        mule.isDonkey # True
    Полиморфизм
    Концепция полиморфизма – важная часть ООП на Python. Все методы в языке изначально виртуальные. Это значит, что
    дочерние классы могут их переопределять и решать одну и ту же задачу разными путями, а конкретная реализация будет
    выбрана только во время исполнения программы. Такие классы называют полиморфными.
        class Mammal:
            def move(self):
            print('Двигается')

        class Hare(Mammal):
            def move(self):
                print('Прыгает')

        animal = Mammal()
        animal.move() # Двигается
        hare = Hare()
        hare.move() # Прыгает
MRO(Method resolution order) - порядок поиска атрибутов при наследовании(child->parent1->parent2)
Виды наследования - моно, множественное(наследование от одного класса и нескольких). Также есть многоуровневое, когда
идет некая матрешка классов
staticmethod vs classmethod - classmethod принимает первым парметорм cls, соответственно он имеет доступ к аттрибутам класса,
чего не имеет staticmethod, оба метода могут вызываться без инициализации объекта
Контекстный менеджер - любой объект, который использует два магических метода - enter(точка входа, к примеру в файл) и
exit(гарантированное закрытие файла), альтернатива - try, except, finally, else(The code enters the else block only if
the try clause does not raise an exception.)
Итератор - любой метод, который реализует магический метод __next__. Итерируемый объект(его цель - создать итератор) реализует метод iter
Генератор - итератор с синтаксическими изменениями(использование опертора yield). Итерируется только один раз(до того,
как не получит exception StopIteration). Без костылей на вторую итерацию не зайти
continue в for просто скпиает итерацию, если условие выполнено
модуль - файл с расширением .py, пакет - это каталог (директория) с файлами модулей, имеющая имя в формате «snake_case»
и содержащая «__init__.py». В папке init'a нет. Инит можно оставить пустым/прописывать зависимости и импорты(импорты будут чище). Он выполняется при каждом импорте пакета
SOLID:
S - simple responsibility(принцип единичной ответственности - каждый класс должен выполнять только те задачи, для которых он был задуман)
O - open/close(принцип открытости/закрытости - Следование принципу OCP заключается в том, что программное обеспечение
изменяется не через изменение существующего кода, а через добавление нового кода. То есть созданный изначально код остаётся
«нетронутым» и стабильным, а новая функциональность внедряется либо через наследование реализации, либо через использование абстрактных интерфейсов и полиморфизм.)
L - The Liskov Substitution Principle(Наследник класса дополняет, но не заменяет поведение базового класса. То есть в любом месте
программы замена базового класса на класс-наследник не должна вызывать проблем. Если по каким-то причинам так не получается,
то вероятнее всего имеет место либо некорректная реализация, либо неверно выбранная абстракция для наследования.
Соблюдение принципа подстановки Барбары Лисков позволяет гарантировать, что любой созданный нами подкласс будет без проблем 
использоваться ранее реализованными модулями, которые работали с надклассом. )
I - interface segregation principle(Принцип разделения интерфейсов говорит о том, что слишком «толстые» интерфейсы
необходимо разделять на более маленькие и специфические)
D - dependency inversion principle(Модуль высокого уровня не должен зависеть от модулей низкого уровня. И то, и другое
должно зависеть от абстракций. )
"""













#enumerate(adds an index to an element of the list):
import json
import string
from string import digits

list_1 = ['History', 'Math', 'Physics', 'CompSci'] #  Лист - итерируемый объект
for index, science in enumerate(list_1, start=1):
    print(index, science)

# values() – данная функция помогает нам получать только значения из словаря, без ключей.
colour = {"Black": 0,
          "Purple": 2,
          "Brown": 4,
          "Yellow": 9,
          "Blue": 1}
list(enumerate(colour.values())) # [(0, 0), (1, 2), (2, 4), (3, 9), (4, 1)]

#list debunked:
print(', '.join(list_1))
#back to list:
a_str = 'a, b, c, d'
print(a_str.split(', '))

#Зачем нужен self
#Это ссылка на экземпляр класса
class Point1:
    color = 'red'
    circle = 2      #|-Point1.get_coords: "who the fuck am giving this method to? Oh, self tells me that it's rock who i give it. Ok then.."
    def get_coords(self, x, y):
        #|-how in the world does rock have an access to y and x, oh right, they have a link - pt.y
        self.y = y
        self.x = x
    def show_coords(self):
        print(self.x, self.y)

'''
rock = Point1()
rock.get_coords(1, 3)
rock.y -- 3
Метод get_coords как был в классе Point1, так и остался, он никуда не передается. Только с помощью ссылки на экземпляр, которой служит self,
мы знаем где этот метод юзается и каким экземпляром. Т.е. метод стоит на месте и служит как экземпляру rock, 
так и может служить экземпляру wood, если он будет создан и метод get_coords будет вызван

Так как методы это тоже аттрибуты класса, то мы можем юзать getattr:
             |-Пространство имен, из которого мы будем брать метод
             |
             |        |-имя метода
f = getattr(rock, 'show_coords')
print(f) -- <bound method Point1.get_coords....>
print(f()) -- (1, 3)
'''

#.set() removes duplicates, changes the order randomly
print({'Ilya', 'Gaimanov', 'Ilya', 'Sam', 'Saam'})
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses)) #.difference as an option .union both combined

#dict.get(key[, default]) -> Значение по ключу, либо default.
my_dict = {'one': 1}
my_dict.get('one')  # 1
my_dict.get('two')  # None
my_dict.get('two', 2)  # 2

#dict.items() -> Представление элементов пары ключ-значение из словаря.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

#map функция, которая позволяет вам преобразовывать весь итерируемый объект с помощью другой функции
def double(x):
    return x * 2
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(double, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]

#zip combines lists into tuples
color = ["Blue", "Orange", "Brown", "Red"]
code = [20, 10, 56, 84]
list(zip(color, code)) # [('Blue', 20), ('Orange', 10), ('Brown', 56), ('Red', 84)]

#обрезать строку после символа
a = 'Моя семья: Папа, Мама, Брат'
a = a.rsplit(':', 1)[0] #'Моя семья'
#is оператор используется для для операций с None, True, False. работает с int, если int(-5, 257)
v = 723
b = 723
#v is b --> False

#super().__init__ Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used
#делегирование!!Можно проворачивать с люыми методами, а не только с init
#btw init -- Метод инициализации
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
square = Square(3, 3)
cube = Cube(3, 3, 3)
print(square.area()) # 9
print(cube.volume()) # 27

# ***********************************
# if __name__ == '__main__'
# ***********************************
# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules
#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run
def main():
    print("Hello!")
if __name__ == '__main__':
    main() # не выполнится, если запустить из другого файла, т.к. __name__ == guide

#lambda применяются там, где нужна маленькая функция на короткое время – например, в функциях высшего порядка,
# таких как map или filter.
my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list) # [18, 5, 12]

#Бывает, нужно вывести элементы итерируемого объекта так, чтобы их разделяли пробелы.
my_list = [1, 2, 3, 5, 7]
print(*my_list) # 1 2 3 5 7

#Функция, содержащая yield, может генерировать сразу несколько результатов. Она приостанавливает выполнение программы,
# отправляет значение результата вызывающей стороне и возобновляет выполнение с последнего yield. Кроме того, функция,
# содержащая yield, отправляет сгенерированную серию результатов в виде объекта-генератора.
myList=[10,20,25,30,35,40,50]
def mod(myList):
    for i in myList:
        if i % 10 == 0:
            yield i
for i in mod(myList):
    print(i) #10 20 30 40 50

#Anotations После двоеточий идут типы, которые принимает аргумент, после -> идет тип, который возвращает функция. Есть варианты, как форсить вбивать именно нужный тип аргумента - Union, Any, Optional
from typing import Optional, Union

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

def hundreds(x: Union[int, float]) -> int:
    return (int(x) // 100) % 10

hundreds(100.0)
hundreds(100)
hundreds("100")  # Argument 1 to "hundreds" has incompatible type "str"; expected "Union[int, float]"

#Типизация: то какой тип аргументов принимает функция и то, какой ти возвращает
def func(number: int, value: list) -> None:
    pass

#seattr присваивает атрибут классу
class Person:
    name = 'Ivan'
    age = 30

setattr(Person, 'lastname', 'Ivanov')# lastname = Ivanov, но аттрибут можно создать и так Person.lastanme = 'Ivanov'
#Удалить аттрибут del Person.lastname

#private whatever. К методам/перемнным, которые начинаются с '__' можно обращаться только внутри класса.
class Bank:
    def __init__(self, man):
        self.__man = man

    def __man_rep(self):
        return f'man name is {self.__man}'
a = Bank('Herbert')
# a.__man Error
# a.__man_rep() Error
'''
Но инкапсуляции полноценной нет, так как доступ можно получить:
a._Bank__man -- Herbert
a._Bank__man = 'Roger'
a._Bank__man -- Roger
'''


# Пространство имен класса
class DptIT:
    PYTHON_DEV = 1
    GO_DEV = 2
    REACT_DEV = 1

    def hiring_devs(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1 # вызывая метод через экземпляр, изменится только переменная экземпляра,
        # и в следующем экземпляре она будет дефолтной
        DptIT.PYTHON_DEV = DptIT.PYTHON_DEV + 1 # тут поменятеся уже переменная класса, и в следующем экземпляре
        # она будет + 1

# Property(свойство)
class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password #Можно присвоить переменной имя сеттера, тогда провреки будут происходить во
        # время создания экземпляра self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError()
        if len(value) < 4:
            raise ValueError()
        if len(value) > 12:
            raise ValueError()
        if not User.is_include_number(value):
            raise ValueError()
        self.__password = value
'''
r = User('aaa', 123)
r.password = [21] -- TypeError('Пароль должен быть строкой')
r.password = '12' -- ValueError('>4 pls')
r.password = '1234567890123456' -- ValueError('<13 pls')
r.password = 'hghjklaa' -- ValueError('digit pls')
r.password = 'sdfghj12' -- OK
'''

#__str__ и __repr__  repr - как наш объект отображается в системе, str - как отображается пользователю

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'
    def __str__(self):
        return f'Lion - {self.name}'
'''
w = Lion('Vasya')
w -- The object Lion - Vasya
print(w) -- Lion - Vasya
str(w) -- Lion - Vasya
'''

#__len__ и __abs__

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname) # Не должно быть отрицательным, поможет abs
                                            # return abs(self) -- сработает как self.__abs__()
    def __abs__(self):
        return abs(self.name - self.surname)
'''
a = Person('aa', 'bbb')
len(a) -- 5 Если бы дандр лен не было - object of type Person has no len()
'''

#__getitem__, __setitem__, __delitem__

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError('out of range')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('list assignment out of range')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('list assignment out of range')
'''
v = Vector(13, 1424, 5, 642, 1)
v[1] -- 1424     Было бы TypeError: 'Vector' object does not support indexing(Классы изначально не поддерживают 
индексацию)
v[0] = 22 -- TypeError: 'Vector' object does not support item assignment, поэтому __setitem__
v[0] = 22
v -- [22, 1424....]
del v[0]
v -- [1424, 5...]
'''

#__iter__

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        return iter(self.surname)

igor = Student('igor', 'nikolaev', [3, 4, 5, 6])
for i in igor:
    print(i) # n i k o l a e v

#__bool__
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x != 0 or self.y != 0

'''
a = Point(3, 4)
bool(a) -- True
или можно вызвать неявно
if a:
    print('Right') -- Right
b = Point(0, 0)
if b:
    print('Right') -- ''
'''

#__call__
from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result

@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *=1
    return pr

'''
fact = Timer(fact)
fact(7) -- Вызывается фунция fact
           Функция отработала за 0.0001...
'''

#everything is object
class Peson:
    pass
'''
issubclass(Person, object) -- True
'''

#Переопределить родительский метод - написать такой же метод, как и у класса-родителя
#Расширить класс - написать метод, которого нет у класса родителя
class Person:
    def breath(self):
        print('breath')
    def walk(self):
        print('walk')
    def combo(self):
        self.walk()
        self.breath()
        if hasattr(self, 'lean'): #Проверка на наличие аттрибута при вызове метода
            print(self.lean)
        if hasattr(self, 'age'):
            print(self.age)
class Doctor(Person):
    age = 30
    def breath(self):
        print('breath!')
    def walk(self):
        print('walk!')
    def lean(self):
        print('lean!')
'''
p = Person()
p.combo -- breath walk
x = Doctor()
x.combo -- breath! walk! lean! 30 
'''

#множественное наследование
class Doctorito:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ura, ya doctor')

class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ura, ya builder')

class Persona(Builder, Doctorito):
    def __init__(self, rank, degree):
        super.__init__(rank)
        Doctorito.__init__(self, degree)

    def __str__(self):
        return f'Person {self.rank}, {self.degree}'

a = Persona(5, 'spec')
a.graduate() # -- Ura, ya builder из-за MRO(method resolution order)
print(a) # -- Person 5 spec

#slots
class Slots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
a = Slots(1, 2)
a.z = 3  # ошибка, так как нельзя присваивать новые аттрибуты классу, где сть slots

#обработка исключений
#Все эксепшены - классы и наследуются от класса baseexception. От него исходят классы exception, systemexit, generator exit и keyboardinterrupt
#От exception исходит AttributeError, ArithmeticError, EOFError, NameError, LookupError(Index&Key errors), OSError, TypeError, ValueError
try:
    1/0
except (ZeroDivisionError, TypeError): # Через запятую несколько исключений указывается
    print('ZeroDivisionError here m8')
else:
    print('good') # выполняется только в при отсутствии ошибок
finally:
    print('end') # выполняется всегда. Нужно юзать когда создаешь файлы, чтобы потом их удалить

#моносостояние python
class User:
    args = {
        'version': 1,
        'flags': 2
    }
    def __init__(self): # Если вводить переменные и нажать alt + enter, можно создать переменную в 3 клика
        self.__dict__ = self.args
'''
a = User()
b = User()
a.args['version'] = 2
a.args['version'] -- 2
b.args['version'] -- 2
'''

#decorators - структурный паттерн. Позволяет расширить функциоанл функции при этом не меняя ее внутри.
def i_am_top(func):
    def wrapper(*args, **kwargs):
        print('I am top!')
        func(*args, **kwargs)
    return wrapper
def pylounge_decorator(hi_msg, bye_msg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(hi_msg)
            func(*args, **kwargs)
            print(bye_msg)
        return wrapper
    return inner_decorator


@i_am_top
@pylounge_decorator('Hello!', 'Bye Everybody!')
def get_something(get1, get2, get3):
    print(f'GET1: {get1},'
          f'GET2: {get2},'
          f'GET3: {get3}')

#Инкремент
a += 1

#замыкания
def func_as_object(a, b):
    def add():
        return a + b
    def sub():
        return a - b
    def mul():
        return a * b
    func_as_object.add = add()
    func_as_object.sub = sub()
    func_as_object.mul = mul()
    return func_as_object

a = func_as_object(1, 3)
'''
a.sub -- -2
a.mul -- 3
'''
def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]
    def func2():
        nonlocal a
        c.append(4)
        a +=1
        return a, b, c
    return func2

'''
a = func1()
a() -- (2, 'line', [1, 2, 3, 4])
a() -- (3, 'line', [1, 2, 3, 4, 4])
'''

# Dictionary comprehensions
import random

dna_bases = ["A", "T", "C", "G"]

dna_st1 = random.choices(dna_bases, k=10)

dna = {key: [b, 'T' if b =='A'
                else 'A' if b =='T'
                else 'C' if b=='G'
                else 'G']
            for (key, b) in enumerate(dna_st1)}

print(dna)
'''
{0: ['A', 'T'], 1: ['A', 'T'], 2: ['C', 'G'], 3: ['C', 'G'], 4: ['T', 'A'], 5: ['C', 'G'], 6: ['A', 'T'], 
7: ['A', 'T'], 8: ['A', 'T'], 9: ['G', 'C']}
'''

keys = ["id", "username", "password"]
users = ["mariyasha888", "KnotABot", "SpongiBOBO", "IAMBATMAN"]
data = [{key:(i if key == "id" else users[i] if key == "username" else "".join(random.choices(string.printable, k=2)))
         for key in keys} for i in range(len(users))]
print(data)
'''
[{'id': 0, 'username': 'mariyasha888', 'password': 'jF'}, {'id': 1, 'username': 'KnotABot', 'password': '?5'}, 
{'id': 2, 'username': 'SpongiBOBO', 'password': '60'}, {'id': 3, 'username': 'IAMBATMAN', 'password': '7V'}]
'''

# for цикл со списком
jj = [1, 2, 3]
for i in range(len(jj)):
    print(i)  # -- wrong!
for i in jj:
    print(i)  # -- right!

print(1_000_000_256)  # 1000000256 More readable
'''
Разница между is и ==
== сравнивает значение операндов(операнд-значение, на которое действует оператор. оператор - имя конкретной операции, выполняемой с операндом(например - +))
is сравнивает то, указывают ли операнды на один и тот же объект в памяти.
Разница между sort и sorted - sort возвращает исходный список, sorted - его копию
del vs pop -- del deletes, pop returns deleted, has default value, if arg not found
функции и методы в Python'e — это практически одно и то же, за исключением того, что методы всегда ожидают первым параметром ссылку на сам объект (self). 
'''

#Линеризация
class A1:
    pass
class A(A1):
    pass
class B(A1):
    pass

class C(A, B):
    pass

'''
Результат наслдеования будет class C(A, B, A1) -- питон автоматом подставит А1, так как это общий родитель
'''

'''
Append vs Extend
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.append(list2) -- [1, 2, 3, 4, [5, 6, 7, 8]]
list1.extend(list2) -- [1, 2, 3, 4, 5, 6, 7, 8]
'''

