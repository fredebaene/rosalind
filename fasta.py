def read_fasta_file(file_directory):

    sequences = {}

    with open(file_directory, "r") as f:

        sequence_id = ""
        sequence = ""
        lines = f.readlines()

        for i in lines:

            if i[0] == ">":

                if lines.index(i) > 0:
                    sequences[sequence_id] = sequence

                sequence_id = i[:-1]

            else:

                sequence += i[:-1]

        sequences[sequence_id] = sequence

    return sequences

if __name__ == "__main__":

    file_directory = input("Please enter the FASTA file directory : ")
    sequences = read_fasta_file(file_directory)
    for k, v in sequences.items():
        print(k, v)
