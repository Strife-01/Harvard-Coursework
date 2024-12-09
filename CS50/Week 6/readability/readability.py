import re


def main() :
    text = get_string("Text: ")
    nr_letters = get_letters(text)
    nr_words = get_words(text)
    nr_sentences = get_sentences(text)
    print_grade(nr_letters, nr_words, nr_sentences)
    return 0


def get_string(string) :
    return input(string)


def get_letters(text) :
    letters_dict = dict()
    for letter in text :
        if letter.isalpha() == True : letters_dict[letter] = letters_dict.get(letter, 0) + 1
    nr_letters = 0
    for letter, num in letters_dict.items() :
        nr_letters += num
    return nr_letters


def get_words(text) :
    return len(re.findall('[\S]+', text))


def get_sentences(text) :
    return len(re.findall('\S[^.!?]*[.!?]', text))


def print_grade(nr_letters, nr_words, nr_sentences) :
    L = 100 * nr_letters / nr_words
    S = 100 * nr_sentences / nr_words
    grade = 0.0588 * L - 0.296 * S - 15.8
    grade = int(grade) if grade - int(grade) < 0.5 else int(grade) + 1
    if grade <= 1 :
        print("Before Grade 1")
    elif grade > 1 and grade < 16 :
        print(f"Grade {grade}")
    elif grade >= 16 :
        print("Grade 16+")


main()
