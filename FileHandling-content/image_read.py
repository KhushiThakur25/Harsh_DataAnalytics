with open('cartoon.png','rb') as file:
    data = file.read()
    print(data)

with open('image_3.png','wb') as file:
    file.write(data)
    