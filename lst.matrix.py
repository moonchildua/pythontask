def print_matrix (rows, col):
    lst =[]
    for j in range (rows):
        counter = j
        my_srt = []
        for dummy_j in range (col):
            counter += 1
            my_srt += str(counter)
        lst = lst + [my_srt]
        print (my_srt)
        return my_srt


def create_list (my_str):  # передаем значение
    converted_to_list = [my_str]   # переменнойconverted_to_list присваиваем  значение element
    print(converted_to_list)
    lst_result = converted_to_list + input_list  #  сделали действие над входным списком и елементом
    return lst_result




row = 2 #int(input(("input row")))
col = 3 #int(input(("input col")))

print_matrix(row,col)