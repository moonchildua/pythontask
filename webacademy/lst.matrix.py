def print_matrix (m, n):
    lst =[]
    counter = 0
    for i in range (m):
        counter = i
        row = []
        for dummy_j in range (n):
            counter += 1
            row.append(counter)
        lst.append(row)
        #print (lst)
    return lst


# row = 2 #int(input(("input row")))
# col = 3 #int(input(("input col")))

print(print_matrix(3, 6))