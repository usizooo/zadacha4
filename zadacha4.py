word_list = (x.lower() for x in  (input("Введите текст:")).split(' '))
unique = set()
for word in word_list:
    if word not in unique:
        unique.add(word)
print(*unique)
