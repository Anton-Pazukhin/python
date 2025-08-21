numbers_1 = [1, 2, 3, 4, 5]


def numbers (number):
    a = sum(number) / len(number)
    return a

print(numbers(numbers_1))

def glas (string):
    wrew = 'aeiouyAEIOUY'
    count = 0
    for x in string:
        if x in wrew:
            count+=1
    return count

print(glas('aeiouyAEIOUY'))

def format_date (*, day: int, month: str)->str:
    return f'The date is {day} of {month}'
print(format_date(day=1, month='may1232tyuty'))