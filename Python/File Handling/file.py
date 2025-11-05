file = open('File Handling/example.txt', 'r')
content = file.read()
print(content)

file.close()

with open('File Handling/example.txt', 'r') as file:
    content = file.readline()
    # print(content)

# with open('File Handling/exam.txt', 'w') as files:
#     files.write("Hello World")

# with open('File Handling/example.txt', 'a') as files:
#     files.write("Hello World")

# with open('File Handling/example.txt', 'r+') as file:
#     content = file.read()
#     print(content)
#     file.write("Hello World")

# with open('File Handling/example.txt', 'w+') as file:
#     content = file.read()
#     print(content)
#     file.write("Hello World")

# with open('File Handling/example.txt', 'a+') as file:
#     file.write("Hello World")
#     file.seek(0)
#     content = file.read()
#     print(content)