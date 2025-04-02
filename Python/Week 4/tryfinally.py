try:
    file = open('error.txt', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()



