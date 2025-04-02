# Simple example of opening a file in read mode
with open('prompts.txt', 'r') as file:
    content = file.read()
    print(content)

# Simple example of opening a file in write mode
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# Simple example of opening a file in append mode
with open('example.txt', 'a') as file:
    file.write('Hello, world!')
