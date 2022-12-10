n, l, r = int(input()), int(input()), int(input())
count = 0
for i in range(l, r + 1):
    for j in range(i, r + 1):
        if i + j == n:
            count += 1
print(count)