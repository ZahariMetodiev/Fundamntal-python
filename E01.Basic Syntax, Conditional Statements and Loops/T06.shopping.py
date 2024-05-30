budget = int(input())

data = input()
flag = True

while data != "End":
    price = int(data)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    data = input()

if flag:
    print("You bought everything needed.")
