def issubset(set1, set2):
    return set1.issubset(set2)


set1 = set(list(map(int, input("Введите первый список чисел: ").split())))
set2 = set(list(map(int, input("Введите второй список чисел: ").split())))
print(issubset(set1, set2))