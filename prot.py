# ROSALIND INFORMATION - ID : PROT - TITLE : TRANSLATING RNA INTO PROTEIN

def translate(mrna_sequence):

    translation_dictionary = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}

    codon_pos = 0
    number_of_codons = len(mrna_sequence) // 3
    protein = ""

    for i in range(number_of_codons):
        codon = mrna_sequence[codon_pos:codon_pos + 3]
        if translation_dictionary[codon] == "Stop":
            return protein
        else:
            protein += translation_dictionary[codon]
            codon_pos += 3

    return protein
