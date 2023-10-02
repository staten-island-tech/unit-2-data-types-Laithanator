subtotal = float(input("Please input subtotal: "))
service = input("State whether your service was bad, okay, good, or excellent: ")
tipPercent = 1
if service == "bad":
    tipPercent = 0
if service == "okay":
    tipPercent = 0.15
if service == "good":
    tipPercent = 0.2
if service == "excellent":
    tipPercent == 0.25
tip = int(subtotal * tipPercent)
print("Your tip is $",(tip))