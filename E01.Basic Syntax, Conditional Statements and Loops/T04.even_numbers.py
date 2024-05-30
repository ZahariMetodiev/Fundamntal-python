n = int(input())
flag = True

for _ in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        flag = False
        break

if flag:
    print("All numbers are even.")
