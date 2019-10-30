# есть игральный кубик который бросают до тех пор, пока не выпадает 6
#
# написать функцию которая имитирует броски кубика и историю просков кубика в виде списка,
# а также возвращает к-ство бросков в виде отдельного числе
#  значение 6 - всегда единственно
#
# def kubik (new_lst):
#      from random import randint
#      lst = []
#      while True:
#           kubik_number = randint(1, 6)
#           if kubik_number != 6 :
#               new_lst = lst +  [kubik_number]
#           else :
#               return  new_lst
#           break
#
# new_lst=[]
# print(kubik(new_lst))
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
def get_num():
    lst = []
    while True:
        dice = random.randint(1,6)
        lst = adding__element (lst, dice)

        if dice == 6:
            break
    num_tries=count_element(lst)

    print(lst)
    print(num_tries)
    print()

get_num()
get_num()

# пустой список - обявляем
# выбросить кубик
# добавить в списое елемент i - функция
# елемент  с кубика сравнить = 6
# если нет то
#     бросаем снова
# если 6 то
#     печатаем список


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
