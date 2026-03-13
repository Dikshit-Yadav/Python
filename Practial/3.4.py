def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

nums = [1, 2, 3, 2, 4, 1, 5]
print("Removed duplicates:", remove_duplicates(nums))
