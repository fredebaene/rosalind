# ROSALIND INFORMATION - ID : PRTM - TITLE : CALCULATING PROTEIN MASS

def calculate_protein_mass(protein):

    file_directory = "./text_files/monoisotopic_amino_acid_masses.txt"
    mass = 0.0

    with open(file_directory, "r") as f:

        masses = {}

        for i in f.readlines():
            aa, aa_mass = i.split(" ", 1)
            masses[str(aa.strip())] = float(aa_mass.strip())

    for i in protein:
        mass = mass + masses[i]

    mass = round(mass, 3)

    return mass

if __name__ == "__main__":

    protein = str(input("Enter the amino acid sequence : "))
    print(calculate_protein_mass(protein))
