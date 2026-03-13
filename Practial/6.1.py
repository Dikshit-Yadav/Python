def read_chars():
    try:
        with open("data.txt", "r") as file:
            content = file.read(50)
            print(content)
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")

read_chars()