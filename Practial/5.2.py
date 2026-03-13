lst = ["apple", "banana", "APPLE", "orange", "banana"]

new_list = []
for i in lst:
    word_upper = i.upper()
    if word_upper not in new_list:
        new_list.append(word_upper)

print("List:", new_list)
