import random


def calculate_magic_numbers(start,end):
    l = []
    for _ in range(5): # صورت سوال گفته یه لیست از اعداد رندوم تو اون بازه باشه و نگفته با چند عنصر
        a = random.randint(start,end)
        l.append(a)
    return l 



a = calculate_magic_numbers(1,10)
print(a) 
