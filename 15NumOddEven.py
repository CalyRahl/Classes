numbers = []

for count in range(15):
    number = int(input("Enter a number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
        