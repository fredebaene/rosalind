# ROSALIND INFORMATION - ID : SPLC - TITLE : RNA SPLICING

import fasta
import rna
import prot

def splicing(sequences):

    sequence_keys = sequences.keys()
    introns = []
    counter = 0

    for i in sequences.keys():
        if counter == 0:
            coding_strand = sequences[i]
            counter += 1
        else:
            introns.append(sequences[i])

    for i in introns:
        coding_strand = coding_strand.replace(i, "")

    return coding_strand

if __name__ == "__main__":

    file_directory = str(input("Enter the FASTA file directory : "))
    sequences = fasta.read_fasta_file(file_directory)
    coding_strand = splicing(sequences)
    mrna = rna.transcribe_as_coding_strand(coding_strand)
    protein = prot.translate(mrna)
    print(protein)
