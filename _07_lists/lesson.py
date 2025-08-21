fruits = ['яблоко', 'груша', 'банан']
fruit = ['слива', 'киви', 'манго']
print(fruits)
fruits2 = list() # пустой список
print(len(fruits)) # длинна списка
print('банан' in fruits) # наличие элемента в списке
element1 = 'яблоко'
element2 = 'груша'
element3 = 'банан'
fruits3 = [element1, element2, element3]
print(fruits3)
fruits.append('апельсин') # добавление элемента в список
print(fruits)
fruits.pop() # удаление последнего элемента в списке
print(fruits)
fruits.extend(fruit)  # объединение списков
print(fruits)
fruits.reverse() # разворот списка
print(fruits)
my_list = [23, 21, 4, 7, 535, 7, 5, 9, 2]
my_list.sort() # сортировка списка по возрастанию
print(my_list)
my_list.sort(reverse=True) # сортировка списка по убыванию
print(my_list)
my_string = 'Форматирование строк в Python с использованием оператора % —'
my_list2 = my_string.split(' ') # разделение строки в список
print(my_list2)