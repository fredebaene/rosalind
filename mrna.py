# ROSALIND INFORMATION - ID : MRNA - TITLE : INFERRING MRNA FROM PROTEIN

def codon_to_amino_acid_mapping(file_directory):

    codons = {}

    with open(file_directory, "r") as f:

        for i in f.readlines():

            if not len(i) == 0:
                codon, aa = i.split(" ", 1)
                codons[codon] = aa[:-1]

    return codons

def number_of_codons_per_amino_acid(file_directory):

    number_of_codons_per_amino_acid = {}

    with open(file_directory, "r") as f:

        for i in f.readlines():

            if not len(i) == 0:
                amino_acid, number = i.split(" ", 1)
                number_of_codons_per_amino_acid[amino_acid] = int(number[:-1])

    return number_of_codons_per_amino_acid

def number_of_mrna_molecules_per_protein(amino_acid_sequence):

    numbers_per_aa = number_of_codons_per_amino_acid("number_of_codons_per_amino_acid.txt")
    n = 1000000
    result = 1

    for i in amino_acid_sequence:

        result *= (numbers_per_aa[i] % n)
        result = result % n

    result *= (numbers_per_aa["Stop"] % n)

    return result

if __name__ == "__main__":

    protein = input("Please enter the amino acid sequence : ")
    result = number_of_mrna_molecules_per_protein(protein)
    print(result)
