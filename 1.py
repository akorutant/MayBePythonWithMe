number = int(input())
z = 0
t = 1
for i in range(9, 1, -1):
    while number % i == 0:
        z += i * t
        t *= 10
        number //= i
if number == 1:
    print(z)
else:
    print(-1)