import cmath
num1 = int(input("Please input your first number to be factored: "))
num2 = int(input("Please input your second number to be factored: "))
gcf = cmath.gcf(num1,num2)
print(gcf)