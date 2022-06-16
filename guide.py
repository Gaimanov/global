#enumerate(adds an index to an element of the list):
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

