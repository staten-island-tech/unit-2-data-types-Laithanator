number = int(input("Please input a number: "))

def operation():
    factor = 0
    divisor = 1
    for i in range(number):
        factor = number % divisor
        if factor == ("0"):
            print(divisor)
        divisor =+ 1
operation()
