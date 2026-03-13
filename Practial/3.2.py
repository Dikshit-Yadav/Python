def reverse_words(str):
    temp = ""
    resStr = ""
    for i in str:   
        if str != " ":
            temp = i + temp
        else:
            resStr += temp + " "
            temp = ""
    resStr += temp
    return resStr

str = input("Enter a line: ")
print("Reversed words:", reverse_words(str))
