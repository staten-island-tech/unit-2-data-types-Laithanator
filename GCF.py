number = int(input("Please input the amount of numbers you're using: "))
divisor = 1
factors = []
def operation(divisor):
    for i in range(facNum):
        factor = facNum % divisor
        if factor == 0:
         print(divisor)
        divisor += 1
for i in range(number):
    facNum = int(input("Please input a number from your list of numbers to be factored: "))
    operation(1)
    factors.extend(divisor)
gcf = max(factors)
print(gcf)