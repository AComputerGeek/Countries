# Author:   Amir Armion
# Version:  V.01


from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    This function takes one parameter(filename), and check its validation (must contain only letters or digits, must
    be length of 1-8 characters, and also has ".txt" at the end of the filename). If the filename wasn't valid, prompt
    the user for another filename. After validating the filename, process the dictionary countries_capitals_dictionary
    and write all information from this dictionary to the filename in the sentence format, for each country one sentence
    in the separate line.
    :param filename: It's a parameter. Must contain only letters or digits, must be length of 1-8 characters, and also
     has ".txt" at the end of the filename.
    :return: Returns all information from the dictionary countries_capitals_dictionary to the filename in the sentence
     format, for each country one sentence in the separate line.
    """
    is_filename = False

    while not is_filename:
        # Checking all restrictions for validating the filename
        if re.search("^[a-zA-Z0-9]{1,8}.txt$", filename):
            print("\"" + filename + "\" is a valid name!")

            f = open(filename, "w")

            for country, capital in countries_capitals_dictionary.items():
                f.write("The capital of %s is %s.\n" % (country, capital))

            f.close()

            is_filename = True
        else:
            # If the filename is not valid, prompt the user to enter another filename
            filename = input("Please enter a valid filename: ")

    # Another way:
    #
    # is_filename = False
    # while not is_filename:
    #     trimmed_filename = filename[0:len(filename) - 4]
    #     if trimmed_filename.isalnum() and 1 <= len(trimmed_filename) <= 8 and filename.endswith(".txt"):
    #         f = open(filename, "w")
    #         for country, capital in countries_capitals_dictionary.items():
    #             f.write("The capital of %s is %s.\n" % (country, capital))
    #         f.close()
    #         is_filename = True
    #     else:
    #         filename = input("Please enter a valid filename: ")
    #         trimmed_filename = filename[0:len(filename) - 4]
    #         if trimmed_filename.isalnum() and 1 <= len(trimmed_filename) <= 8 and filename.endswith(".txt"):
    #             print("Now, the file name is valid!")


def save_capitals():
    """
    This function opens files for writing only.
    :return: Returns a file of all capital names which is contains three consecutive vowels,
     returns a file of all capital names which is contains three consecutive consonants,
     returns a file of all capital names which is contains 'i' somewhere before 'e',
     returns a file of all capital names which is starts with 'a' and ends with 'a',
     returns a file of all capital names which is ends with a vowel,
     returns a file of all capital names which is contains apostrophe, space or x,
     and returns a file of all capital names which is not start with a-e, l-p or s.
    """
    f = open("vowel_vowel_vowel.txt", "w")

    for capital in capitals:
        # Checking the capitals who contains three consecutive vowels
        if re.search("[aeiou]{3}", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # vowels = ("a", "e", "i", "o", "u")
    #
    # f = open("vowel_vowel_vowel.txt", "w")
    # for capital in capitals:
    #     i = 0
    #     while i < len(capital) - 2:
    #         if capital[i].lower() in vowels and capital[i + 1].lower() in vowels and capital[i + 2].lower() in vowels:
    #             f.write(capital + "\n")
    #             break
    #         i += 1
    # f.close()

    f = open("cons_cons_cons.txt", "w")

    for capital in capitals:
        # Checking the capitals who contains three consecutive consonants
        if re.search("[^aeiou ,.'()-]{3}", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # special = (" ", "(", ")", "'", ".", "-", "_")
    # f = open("cons_cons_cons.txt", "w")
    # for capital in capitals:
    #     i = 0
    #     while i < len(capital) - 2:
    #         if capital[i].lower() not in vowels and capital[i + 1].lower() not in vowels and \
    #                 capital[i + 2].lower() not in vowels:
    #             if capital[i] not in special and capital[i + 1] not in special and capital[i + 2] not in special:
    #                 f.write(capital + "\n")
    #                 break
    #         i += 1
    # f.close()

    f = open("i_before_e.txt", "w")

    for capital in capitals:
        # Checking the capitals who contains "i" somewhere before "e"
        if re.search("[i]+[a-z ,.'()-]*[e]+", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # f = open("i_before_e.txt", "w")
    # for capital in capitals:
    #     i = 0
    #     while i < len(capital):
    #         if capital[i].lower() == "i":
    #             j = i
    #             while j < len(capital):
    #                 if capital[j].lower() == "e":
    #                     f.write(capital + "\n")
    #                     break
    #                 j += 1
    #             break
    #         i += 1
    # f.close()

    f = open("a_a.txt", "w")

    for capital in capitals:
        # Checking the capitals who starts with "a" and also ends with "a"
        if re.search("^[a][a-z ,.'()-]*[a]$", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # f = open("a_a.txt", "w")
    # for capital in capitals:
    #     if capital.lower().startswith("a") and capital.lower().endswith("a"):
    #         f.write(capital + "\n")
    # f.close()

    f = open("end_with_vowel.txt", "w")

    for capital in capitals:
        # Checking the capitals who ends with a vowel
        if re.search("[aeiou]$", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # f = open("end_with_vowel.txt", "w")
    # for capital in capitals:
    #     if capital[-1] in vowels:
    #         f.write(capital + "\n")
    # f.close()

    f = open("weird.txt", "w")

    for capital in capitals:
        # Checking the capitals who contains apostrophe, space or x
        if re.search("[' x]", capital):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # weird = (" ", "'", "x")
    #
    # f = open("weird.txt", "w")
    # for capital in capitals:
    #     i = 0
    #     while i < len(capital):
    #         if capital[i] in weird:
    #             f.write(capital + "\n")
    #             break
    #         i += 1
    # f.close()

    f = open("not_start.txt", "w")

    for capital in capitals:
        # Checking the capitals who does not start with a-e, l-p, or s
        if re.search("^[^[a-el-ps]", capital, re.IGNORECASE):
            f.write(capital + "\n")

    f.close()

    # Another way:
    #
    # forbidden_letters = ("a", "b", "c", "d", "e", "l", "m", "n", "o", "p", "s")
    #
    # f = open("not_start.txt", "w")
    # for capital in capitals:
    #     if capital[0].lower() not in forbidden_letters:
    #         f.write(capital + "\n")
    # f.close()


def main():
    print("I should not be called!")


if __name__ == "__main__":
    main()
