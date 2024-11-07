"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""
"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""

def reverse_complement(dna_sequence):
    """ A function that returns the reverse complement of a DNA sequence"""

    complement = ""
    for base in dna_sequence:

        if base == "A":
            new_base = "T"
        
        elif base == "T":
            new_base = "A"
        
        elif base == "G":
            new_base = "C"
        
        else:
            new_base = "G"
        
        complement += new_base

    return complement[::-1]

if __name__ == "__main__":
    dna_sequence = "ATGATCTCGTAA"
    reverse_complement_sequence = reverse_complement(dna_sequence)
    print (dna_sequence)
    print(reverse_complement_sequence)