# def my_sum (x, y):
#     return x+y
#
# res = my_sum(2, 3)
# print(res)


# def square ():
#     for num in range (1, 6):
#         print(num**2)
#
# square()


def square (max_num):
    lst = []
    for num in range (1, max_num+1):
        lst.append(num**2)
    return lst

print(square(10))
print(square(3))