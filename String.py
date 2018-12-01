# print('"Isn\'t", she said.')
# print("Hello\nworld")
# print('c:\some\name')
# print(r'c:\some\name')
#
# print('3'+ ' ' + '3')




#word = "Python"
#assert word[0] == "P"
#assert word[2:5] == "tho"
#assert word[-2] == "o"
#assert word[0:2] == "Py"
#assert word[4:] == "on"
#assert word[:2] + word[2:] == "Python"
#assert word[4:42] == "on"
#assert word[42:] == "on"

# for letter in "Python":
#     print(letter)

# for letter in "Python":
#     print(letter, end="\n")

# suquares = [1, 3, 9, 16, 25]

#assert suquares [0] == 1
#assert suquares [0] == 2

# for letter in "Python":
#     print(letter, end="1")

# word = "Python"
# print(word[5:1:-1])
#
# word = "Python"
# print(word[6::-1])



# def count_letter (input_word, in_letter):
#     """
#         Написать функцию, которая принимает строку и символ.
#         Возвращает количество заданных символов в строке, учитывая регистр.
#         count_char("Hello world", "o") == 2
#         count_char("Hello world", "d") == 1
#         count_char("Hello world", "z") == 0
#     :param input_word : string
#     :param in_letter : one char string
#     :return; int
#     """
#     counter = 0
#     for letter in input_word:
#         if letter == in_letter:
#             counter += 1
#     return counter
#
# praze = "Hello world"
# in_letter = input("type letter")
#
# result = count_letter(praze, in_letter)
# print(result)


# assert  count_letter(praze, 'o') == 2
# assert  count_letter(praze, 'd') == 1
# assert  count_letter(praze, 'a') == 0

lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = lst1[:]

lst1[0] = 99

print(lst1)
print(lst2)

