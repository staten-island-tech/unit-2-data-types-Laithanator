number = int(input("Please state your number to be factored: "))
def operation():
    divisor = 1
    for i in range(number):
        factor = number % divisor
        if factor == 0:
         print(divisor)
        divisor += 1
operation()