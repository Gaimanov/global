#enumerate(adds an index to an element of the list):
from string import digits

list_1 = ['History', 'Math', 'Physics', 'CompSci']
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
print(a_str.split(','))

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
        if(i%10==0):
            yield i
for i in mod(myList):
    print(i) #20 30 40 50

#Anotations После двоеточий идут типы, которые принимает аргумент, после -> идет тип, который возвращает функция.
def func(number: int, value: list) -> None:
    pass

#seattr присваивает атрибут классу
class Person:
    name = 'Ivan'
    age = 30

setattr(Person, 'lastname', 'Ivanov')# lastname = Ivanov, но аттрибут можно создать и так Peson.lastanme = 'Ivanov'
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