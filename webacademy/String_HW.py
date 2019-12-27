def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'

    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    # assert correct_sentence("hi") == "Hi."
    # assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")


    # def correct_sentence(text: str) -> str:
    #     return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.replace(',', ' ').replace('.', ' ')  #return text.lstrip('., ').replace('.', ' ').split()[0].rstrip(', ')
    text = text.split()
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")