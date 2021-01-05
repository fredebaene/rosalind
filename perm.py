# ROSALIND INFORMATION - ID : PERM - TITLE : ENUMERATING GENE ORDERS

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, total):

    permutations = []
    elements = []
    for i in range(n):
        elements.append(i + 1)
    counters = []
    denominator = total / n

    for i in range(total):
        permutation = []
        permutation.append(int((i // denominator) + 1))
        permutations.append(permutation)

    for i in range(1, n):
        grouping = factorial(n - i)
        indexing_denominator = factorial(n - i - 1)
        indexing_numerator = -1
        s = -1
        for j in range(total):
            remainder = j // grouping
            if remainder > s:
                s = remainder
                indexing_numerator = 0
                unused_elements = [x for x in elements if x not in permutations[j]]
            index = (indexing_numerator // indexing_denominator)
            permutations[j].append(unused_elements[index])
            indexing_numerator += 1

    return permutations

if __name__ == "__main__":

    n = int(input("Please enter a number : "))
    number_of_permutations = factorial(n)
    print(number_of_permutations)
    permutations = permutations(n, number_of_permutations)
    print(permutations)
