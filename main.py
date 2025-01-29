"""bookbot project """


def read_book_content(file_path):
    """read file content"""
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents


def count_words(string):
    """count the number of words in a string"""
    words_number = len(string.strip().split())

    return words_number


def count_character_frequency(string):
    """count the number of times each character appears
    in the string, case-insensitive."""
    string = string.lower()
    frequency_dict = {}
    for i in string:
        if i.isalpha():
            if i not in frequency_dict:
                frequency_dict[i] = 1
            else:
                frequency_dict[i] += 1

    return frequency_dict


def sort_dict_by_values(dictionary, reverse=True):
    """sort dictionary by its value"""
    sorted_by_value = sorted(
        dictionary.items(), key=lambda item: item[1], reverse=reverse
    )
    sorted_dict = {}
    for key, value in sorted_by_value:
        sorted_dict[key] = value

    return sorted_dict


def main():
    """main function"""
    file_path = "books/frankenstein.txt"
    file_contents = read_book_content(file_path)
    words_number = count_words(file_contents)
    frequency_dict = count_character_frequency(file_contents)
    sorted_frequency_dict = sort_dict_by_values(frequency_dict)
    print(f"--- Begin report of {file_path} ---".center(50, "-"))
    print(f"{words_number} words found in the document")
    for i, j in sorted_frequency_dict.items():
        print(f"The '{i}' character was found {j:5} times")
    print(f"{"End report":-^50}")


main()
