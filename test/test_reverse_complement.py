import unittest
from reverse_complement import reverse_complement

class TestReverseComplement(unittest.TestCase):

    def test_reverse_complement(self):
        """Reverse Complement of a DNA sequence"""
        dna_sequence = "ATGATCTCGTAA"
        reverse_complement_sequence = reverse_complement(dna_sequence)
        self.assertEqual(reverse_complement_sequence, "TTACGAGATCAT")

    def test_reverse_complement_unkown_letters(self):
        """Reverse Complement of a DNA sequence more robust"""
        dna_sequence = "ATGATCTCGTAAa"
        reverse_complement_sequence = reverse_complement(dna_sequence)
        self.assertEqual(reverse_complement_sequence, "TTACGAGATCAT")