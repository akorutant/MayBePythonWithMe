old_string = input()
new_string = ''
for i in old_string:
    new_string += chr(97 + 122 - ord(i))
print(new_string)