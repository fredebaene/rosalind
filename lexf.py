# ROSALIND INFORMATION - ID : LEXF - TITLE : ENUMERATING K-MERS LEXICOGRAPHICALLY

def all_strings(alphabet, string_length):

    strings = []
    number_of_letters = len(alphabet)
    number_of_strings = number_of_letters ** string_length

    grouping = number_of_strings / number_of_letters
    for i in range(number_of_strings):
        index = int(i // grouping)
        string = alphabet[index]
        strings.append(string)

    for i in range(string_length - 1):
        grouping = number_of_strings / (number_of_letters ** (i + 1))
        indexing_numerator = -1
        indexing_denominator = number_of_strings / (number_of_letters ** (i + 2))
        s = -1
        for j in range(len(strings)):
            remainder = j // grouping
            if remainder > s:
                s = remainder
                indexing_numerator = 0
            index = int(indexing_numerator // indexing_denominator)
            indexing_numerator += 1
            strings[j] += alphabet[index]

    return strings

if __name__ == "__main__":

    user_input = str(input("Please enter the alphabet : "))
    string_length = int(input("Please enter string length : "))
    alphabet = user_input.split(" ")
    strings = all_strings(alphabet, string_length)
    for i in strings:
        print(i)
