#enumerate(adds an index to an element of the list):
list_1 = ['History', 'Math', 'Physics', 'CompSci']
for index, science in enumerate(list_1, start=1):
    print(index, science)
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

#dict.items() -> Представление элементов словаря.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

#zip combines lists into tuples
def func2(list1, list2, num):
    return dict(zip(list1[:num], list2))
#обрезать строку после символа
a = 'Моя семья: Папа, Мама, Брат'
a = a.rsplit(':', 1)[0] #'Моя семья'
