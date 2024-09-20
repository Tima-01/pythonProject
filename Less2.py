def find_longest_word_space(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word


def find_longest_word_semicolon(sentence):
    words = sentence.split(';')
    longest_word = max(words, key=len)
    return longest_word


def find_shortest_word(sentence, delimiter):
    words = sentence.split(delimiter)
    shortest_word = min(words, key=len)
    return shortest_word


def find_word_in_sentence(sentence, word):
    if word in sentence:
        return f"Слово '{word}' найдено в строке."
    else:
        return f"Слово '{word}' не найдено в строке."


def count_words(sentence):
    words = sentence.split()
    return len(words)


def main():
    while True:
        print("\nВыберите задачу:")
        print("1. Найти самое длинное слово (разделитель — пробел)")
        print("2. Найти самое длинное слово (разделитель — точка с запятой)")
        print("3. Найти самое короткое слово по указанному разделителю")
        print("4. Найти указанное слово в строке")
        print("5. Посчитать количество слов в предложении")
        print("6. Выйти")

        choice = input("Введите номер задачи: ")

        if choice == "1":
            sentence = input("Введите предложение: ")
            print("Самое длинное слово:", find_longest_word_space(sentence))
        elif choice == "2":
            sentence = input("Введите строку с разделителем ';': ")
            print("Самое длинное слово:", find_longest_word_semicolon(sentence))
        elif choice == "3":
            sentence = input("Введите строку: ")
            delimiter = input("Введите разделитель: ")
            print("Самое короткое слово:", find_shortest_word(sentence, delimiter))
        elif choice == "4":
            sentence = input("Введите строку: ")
            word = input("Введите слово для поиска: ")
            print(find_word_in_sentence(sentence, word))
        elif choice == "5":
            sentence = input("Введите предложение: ")
            print("Количество слов в предложении:", count_words(sentence))
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main()
