# ROSALIND INFORMATION - ID : LGIS - TITLE : LONGEST INCREASING SUBSEQUENCE

def read_file(file_directory):

    with open(file_directory, "r") as f:

        sequence = f.readlines()[1]

    return sequence

def longest_increasing_subsequence(sequence):

    lengths = []
    sequences = []

    for i in range(len(sequence)):

        lengths.append(1)
        sequences.append(str(sequence[i]))

    for i in range(1, len(sequence)):

        for j in range(0, i):

            if (sequence[i] > sequence[j]) and ((lengths[j] + 1) > lengths[i]):

                lengths[i] = lengths[j] + 1
                sequences[i] = sequences[j] + " " + str(sequence[i])

    longest_increasing_subsequence = sequences[lengths.index(max(lengths))]

    return longest_increasing_subsequence

def longest_decreasing_subsequence(sequence):

    lengths = []
    sequences = []

    for i in range(len(sequence)):

        lengths.append(1)
        sequences.append(str(sequence[i]))

    for i in range(1, len(sequence)):

        for j in range(0, i):

            if (sequence[i] < sequence[j]) and ((lengths[j] + 1) > lengths[i]):

                lengths[i] = lengths[j] + 1
                sequences[i] = sequences[j] + " " + str(sequence[i])

    longest_decreasing_subsequence = sequences[lengths.index(max(lengths))]

    return longest_decreasing_subsequence

if __name__ == "__main__":

    file_directory = "lgis.txt"
    sequence = read_file(file_directory)
    sequence = sequence[:-1]
    sequence = list(map(int, sequence.split(" ")))
    lis = longest_increasing_subsequence(sequence)
    lis_string = ""
    for i in lis.split(" "):
        lis_string += i + " "
    lis_string = lis_string[:-1]
    lds = longest_decreasing_subsequence(sequence)
    lds_string = ""
    for i in lds.split(" "):
        lds_string += i + " "
    lds_string = lds_string[:-1]
    print(lis_string)
    print(lds_string)
