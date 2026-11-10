
import unittest

from dna_analyzer import (
    validate_dna,
    calculate_gc_content,
    get_complement,
    get_reverse_complement
)


class TestDNAAnalyzer(unittest.TestCase):

    # Test DNA validation

    def test_valid_sequence(self):

        result = validate_dna("atgc")

        self.assertEqual(result, "ATGC")

    # Test sequence length indirectly

    def test_sequence_length(self):

        result = analyze_length("ATGC")

        self.assertEqual(result, 4)

    # Test GC content

    def test_gc_content(self):

        result = calculate_gc_content("ATGC")

        self.assertEqual(result, 50.0)

    # Test 100% GC content

    def test_high_gc_content(self):

        result = calculate_gc_content("GGGGCCCC")

        self.assertEqual(result, 100.0)

    # Test 0% GC content

    def test_low_gc_content(self):

        result = calculate_gc_content("ATATAT")

        self.assertEqual(result, 0.0)

    # Test complementary DNA

    def test_complement(self):

        result = get_complement("ATGC")

        self.assertEqual(result, "TACG")

    # Test reverse complement

    def test_reverse_complement(self):

        result = get_reverse_complement("ATGC")

        self.assertEqual(result, "GCAT")

    # Test invalid DNA

    def test_invalid_sequence(self):

        with self.assertRaises(ValueError):

            calculate_gc_content("ATGX")

    # Test empty DNA

    def test_empty_sequence(self):

        with self.assertRaises(ValueError):

            calculate_gc_content("")


# Helper function for testing length

def analyze_length(sequence):

    return len(validate_dna(sequence))


if __name__ == "__main__":

    unittest.main()
