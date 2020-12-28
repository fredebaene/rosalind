# ROSALIND INFORMATION - ID : ORF - TITLE : OPEN READING FRAMES

import revc
import mrna

def set_of_coding_strands(sequence):

    reverse_complement = revc.reverse_complement(sequence)
    set_of_coding_strands = []

    for i in range(3):

        number_of_codons = len(sequence[i:]) // 3
        stop = i + (number_of_codons * 3)
        set_of_coding_strands.append(sequence[i:stop])

    for i in range(3):

        number_of_codons = len(reverse_complement[i:]) // 3
        stop = i + (number_of_codons * 3)
        set_of_coding_strands.append(reverse_complement[i:stop])

    return set_of_coding_strands

def locate_open_reading_frames(sequence):

    open_reading_frames = []
    number_of_codons = len(sequence) // 3
    codons = ["ATG", "TAA", "TAG", "TGA"]
    first = []
    last = 0
    start = False

    for i in range(number_of_codons):

        pos = 0 + (i * 3)

        if sequence[pos:pos + 3] in codons:

            if sequence[pos:pos + 3] == "ATG":

                start = True
                first.append(int(pos))

            elif sequence[pos:pos + 3] != "ATG" and start == True:

                last = pos
                for j in first:
                    orf = (j, last)
                    open_reading_frames.append(orf)
                start = False
                first = []
                last = 0

    return open_reading_frames

def dna_to_protein(sequence, dna_codons):

    number_of_codons = len(sequence) // 3
    protein = ""

    for i in range(number_of_codons):

        pos = 0 + (i * 3)
        protein += dna_codons[sequence[pos:pos + 3]]

    return protein


if __name__ == "__main__":

    sequence = input("Please enter the DNA sequence : ")
    file_directory = "./text_files/dna_codons.txt"
    dna_codons = mrna.load_codons(file_directory)
    proteins = []

    set_of_coding_strands = set_of_coding_strands(sequence)

    for i in set_of_coding_strands:

        open_reading_frames = locate_open_reading_frames(i)

        for j in open_reading_frames:

            x, y = j
            protein = dna_to_protein(i[x:y], dna_codons)
            proteins.append(protein)

    for i in set(proteins):
        print(i)
