num1 = int(input("State your first number: "))
num2 = int(input("State your second number: "))
list1 = []
list2 = []
list3 = []
for i in range(1, num1 + 1):
    if num1 % i == 0:
        list1.extend([i])

for i in range(1, num2 + 1):
    if num2 % i == 0:
        list2.extend([i])

high1 = list1[-1]
high2 = list2[-1]
highNum = 1

if high1 > high2:
    highNum = int(list1[-1])
else:
    highNum = int(list2[-1])

count = 0

for i in range(highNum):
    m = list1[count]
    if list1[count] == list2[count]:
        list3.extend(m)
    count += 1
print(list3[-1])