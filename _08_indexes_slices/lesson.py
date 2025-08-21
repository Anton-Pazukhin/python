fruits = ['apple', 'banana', 'cherry']
print(fruits[0]) # поиск элемента по индексу
fruits[0] ='melon' # присвоение элементу другого значения
print(fruits)
fruits[0], fruits[2] = fruits[2], fruits[0] # перестановка местами элементов 0 и 2
print(fruits)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:4]) # выводим первые 4 элемента
print(numbers[:4]) # выводим первые 4 элемента
print(numbers[:]) # выводим все элементы
print(numbers[::2]) # выводим все элементы с шагом 2, каждый второй
print(numbers[::-1]) # развернули список
numbers.reverse() # развернули список способ 2
print(numbers)
new_numbers = list(reversed(numbers)) # развернули список способ 3
print(new_numbers)