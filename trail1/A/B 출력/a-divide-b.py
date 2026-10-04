# format 함수로 소수점 20번째까지 값 올바르게 구할 수 없다 
# f 써도 중간부터 근삿값이 되버려 구할 수 없음 .:f 는 버림이 아니라 반올림

a, b = map(int, input().split())

print(f"{a//b}.", end = "")

# 나머지 구하는 연산자 
a %= b

for i in range(20):
    a *= 10 # 나머지에 10을 곱한 값을 기준으로 계산
    print(a // b, end = "")

    a %= b