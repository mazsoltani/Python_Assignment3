length = int(input("Please Enter  a number="))

snake= []

for i in range(length):
    if (i % 2 == 0):
        snake.append("*")
    else:
        snake.append("#")

print(snake)