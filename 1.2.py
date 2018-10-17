# #n += 1
# n = 1
# while n < 5:
#     n += 1
#     print(n**2)
#
#
# for n in [1,2,3,4,5]:
#     print(n, "**2", n**2)

# for animals in ["cat", "dog", "elephant"]:
#     print(animals)

# for animal in ["cat", "dog", "elephant"]:
#     if animal == "cat":
#         print("Hello", animal)
#     else:
#         print("go away!", animal)


# rng = range(6)
# print(list(rng))

# rng = range(3, 6, 2)
# print(list(rng))

# for num in range(1, 6):
#     print(num**2)

# Home Work 1
# n = int (input("Please write number, "))
# if n%3 == 0 and n%5 == 0:
#     print("Fizz Buzz")
# if n%3 == 0:
#     print("Fizz")
# elif n%5 == 0:
#     print("Buzz")
# else:
#     print("n= ", n)

# Home Work 1
# n = int (input("please enter number "))
# def square_event ():
#     lst = []
#     for num in range (1, n+1):
#         if num % 2 == 0:
#             lst.append(num**2)
# #  collumn          num=num**2
# #  collumn          print(num)
#     print(lst)
# square_event()

# Simple function without condition
# def index (m, n):
#         num_squar = m[n] ** n
#         print(num_squar)
#
#
# n = int (input("Please write number, "))
# m = [1, 3, 10, 100]
# index ( m, n)

# thing_index = thing_list.index(elem) if elem in thing_list else -1

# def index (m,n):
#     # if m[n] is True:
#     #     num_squar = m[n] ** n
#     #     print (num_squar)
#     if len(m) <= n :
#         num_squar = -1
#         print(num_squar)
#     else:
#         num_squar = m[n] ** n
#         print(num_squar)
#
#
#
# n = int(input("Please write number, "))
# m = [1, 2]
# index(m,n)

# Initial datas
#Условие: Дан список с положительными числами и число N. Написать
# функцию, которая находит N-ую степень элемента в массиве с индексом N.
# Если N за границами массива, тогда вернуть -1.
# *Не забывайте, что первый элемент имеет индекс 0.
# index_power = ([1, 2, 3, 4], n)
# index_power = ([1, 3, 10, 100], n )
# index_power = ([0, 1], n)
# index_power = ([1, 2], n)


def index (m,n):
    # if m[n] is True:
    #     num_squar = m[n] ** n
    #     print (num_squar)
    if len(m) <= n :
        num_squar = -1
        print ("n", num_squar)
    else:
        num_squar = m[n] ** n
        print("m(n) ** n = ", num_squar)



n = int(input("Please write number, "))
m = [1, 3, 10, 100]
index(m,n)
print (m,n)