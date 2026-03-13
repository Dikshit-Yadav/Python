def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

str = input("Enter a string: ")
print("vowels:", count_vowels(str))
