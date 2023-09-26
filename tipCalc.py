bill = input("Please input bill amount: ")
bill = float(bill)
tipPercent = input("Please input tip percentage (only use numbers, no percent symbol): ")
tipMult = tipPercent * 0.01
tipMult = float(tipMult)
tip = bill * tipMult
tip = int(tip)
total = tip + bill
print("Bill:",(bill),"Tip:",(tip),"Total:",(total))