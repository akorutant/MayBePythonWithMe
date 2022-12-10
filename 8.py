time = [int(i) for i in input().split(":")]
if time[0] < 24 and time[1] < 60:
    print(True)
else:
    print(False)