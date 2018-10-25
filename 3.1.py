# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, "equals", x, "*", n//x)
#             break
#     else:
#         print(n, "os prime number (prostoe chislo)")

# n==4, range(2, 4) -> (2, 3)
# x ==2, 4 & 2 == 0, 4 == 2 * 2

# n == 5, range(2, 5) -> [2, 3, 4]
# x == 2, 5 % 2 == 1
# x == 3, 5 % 2 == 2
# x == 4, 5 % $ == 1
# 5 is prime munber

# while True:
#     command = input("enter command: ")
#     if command in ["exit", 'quit']:
#         print("bye-bye!")
#         break
#     else:
#         print("command: ", command)


# for num in range(2, 10):
#     if num % 3 == 0:
#         print("found number multiple of three ", num)
#         continue
#     print("number", num)

# def multiple(n):
#     for num in range(2, n):
#         if num % 3 == 0:
#             print("found number multiple of three ", num)
#             continue
#         print("number", num)
#
# multiple(5)
# multiple(10)

# import math
# print(math.pi)

# import random
# print(random.randint(1, 9))

# from random import randint
# from math import  pi
#
# for i in range (10):
#     print(pi * randint(1, 9))


# def multiple(tries,m):
#     from math import pi
#     from random import randint
#     for i in range(tries):
#        print('multi n*pi = ',  pi * randint(1, m))
#
# multiple(9,5)


def multiple(tries,m):
    from math import pi
    from random import randint as lol
    for i in range(tries):
       print('multi n*pi = ',  pi * lol(1, m))

multiple(5,5)