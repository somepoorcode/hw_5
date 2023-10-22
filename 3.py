set1_n = int(input("Введите кол-во названных городов:\n"))
set1 = set()

print("Введите ранее названные города:")
for i in range(set1_n):
    set1.add(str(input()))

set2 = set()
set2.add(str(input("Введите новый город:\n")))

if set1.intersection(set2):
    print("\nREPEAT")
else:
    print("\nOK")