a, b = map(int, input().split())

print(a, end = " ")
while a <= b:
    if a % 2 == 0:
        a += 3
    elif a % 2 == 1:
        a = a * 2
    
    if a <=b:
        print(a, end = " ")

        