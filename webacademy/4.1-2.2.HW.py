import random
def adding__element (input_list, element):  # передаем значение
    converted_to_list = [element]           # переменнойconverted_to_list присваиваем  значение element
    lst_result = input_list + converted_to_list #  сделали действие над входным списком и елементом
    return lst_result  # вернули результат

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


from random import randint
def get_num(bingo_num):
    lst = []
    if bingo_num > 6:
        bingo_num = 6
    if bingo_num <= 0:
        bingo_num = 1
    while True:
        dice = random.randint(1,6)
        lst = adding__element (lst, dice)
        if dice == bingo_num:
            break
    num_tries=count_element(lst)
    print(lst)
    print(num_tries)
    print()

get_num(5)
get_num(100)
get_num(-6)