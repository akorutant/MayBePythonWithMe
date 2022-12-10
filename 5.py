import string

input_count = int(input())
input_string = input().translate(str.maketrans
                                 ('', '', string.punctuation)).replace('“', "").replace("”", "").split()
count = 0

for i in input_string:
    if len(i) <= input_count and i.isalpha():
        count += 1

print(count)