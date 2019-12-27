

# assert  suquares [-1] == 25
#
# cubes = [1, 8, 27, 65, 125]
# assert  cubes + [36, 55] == [1, 8, 27, 65, 125, 36, 55]
#
# cubes = [1, 8, 27, 65, 125]
# cubes [3] == 4**3 # замена по елементу индекса
# assert  cubes == []

#a = 3
#print([a])
#print([1, 2]+ [a])

#print([1+2]+ [3+4])

#написать функцию которая добавляет заданный элемент в конец списка и возварщает этот список

# def adding__element ():
#     lst = [1, 2, 3]
#     new_lst = lst + [n]
#     print(new_lst)
#     return (new_lst)
#
# n = int(input("input n "))
# adding__element()


# def adding__element (lst, element):
#     return lst + [element]
#
# print(adding__element([1, 2, 3],3))



# def adding__element (input_list, element):  # передаем значение
#     converted_to_list = [element]           # переменнойconverted_to_list присваиваем  значение element
#     lst_result = input_list + converted_to_list #  сделали действие над входным списком и елементом
#     return lst_result  # вернули результат
#     #return lst + [element] - это кратко без 3 предыдущих строк
#
# initial_lst = [1, 2, 3]
# add_element = 77
#
# result_list = adding__element(initial_lst, add_element)
#
# #print(result_list)
# for num in result_list:
#     print(num)

def count_element (input_list):
    """
    [1,2,3] -> 3
    ['a'] ->1
    ['a', 'b'] -> 2
    :param input_list: list
    :return: int
    """
    counter = 0
    for dummy_i in input_list:
        counter +=1
    return counter

print(count_element([1, 2, 3, 7, 8]))

