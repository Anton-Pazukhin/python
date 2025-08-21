file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
for x in file_names:
    print(x)
greeting = 'Hello, World!'
count = 0
for x in greeting:
    if x == 'o':
        count += 1
print(count)
students = ["Alice", "Bob", "Charlie", "David"]
for x in students:
    print(x)
    for xx in x:
        print(xx)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for x in numbers:
    if x == 10:
        break
    elif x % 2== 0:
       continue
    else: print(x)

    # Функция range
range_object = list(range(10))
print(range_object)
numbers2 = [1, 2, 3, 4, 5, 6]
numbers3 = []
for x in numbers2:
    numbers3.append(x+1)
print(numbers3)
for i in range(len(numbers)):   # Берём индексы элементов нашего списка
    numbers[i] += 1              # Увеличиваем значение текущего элемента на 1

greeting = 'Hello, World!'
count = 0
greet = []
for i in range(len(greeting)):
    if greeting[i]  == 'o':
        count +=1
        greet.append(i)
print(count)
print(greet)

