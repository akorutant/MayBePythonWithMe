number = input()
current_min = -1

for i in range(len(number)):
    new = number
    new = list(new)
    new.pop(i)
    new = "".join(new)

    if int(new) > current_min or current_min == -1:
        current_min = int(new)

print(current_min)
