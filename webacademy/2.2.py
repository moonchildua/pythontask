# # #n += 1
# n = 0
# while n < 5:
#     print(n**2)
#     n += 1


# for n in [1,2,3,4,5]:
#     print(n, "**2", n**2)

# for animals in ["cat", "dog", "elephant"]:
#     print(animals)

# for animal in ["cat", "dog", "elephant"]:
#     if animal == "cat":
#         print("Hello", animal)
#     else:
#         print("go away!", animal)

# rng = range (3, 6, 2)
# print(list(rng))

# def my_sum():
#     for num in range(1, 6):
#         print (num ** 2)
#
# result = my_sum()

# def square (x):
#     lst = []
#     for num in range (1, x+1):
#         lst.append(num**2)
#     return lst
#
# print(square(10))


# Home Work 1

def check_if ():
    if n%3 == 0 and n%5 == 0:
        print("Fizz Buzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print("n= ", n)


n = int (input("Please write number, "))
check_if()