n = int(input("Ведите число: "))

if n < 0:
    n = 0
    print("Zero, ")
if n == 0:
    print("you enter Zero")
elif n % 2 == 1:
    print("NeChet")
else:
    print("Chet")



