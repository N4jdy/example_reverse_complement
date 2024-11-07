# Reverse Complement of DNA Sequence
The genetic code of a cell is stored in the DNA, which is a double-stranded molecule. Each strand of DNA is a chain of nucleotides, matching each other in a complementary fashion. The four types of nucleotides are adenine (A), cytosine (C), guanine (G) and thymine (T). The nucleotides are complementary in the following way: A always pairs with T, and C always pairs with G. Hence, the reverse complement of a DNA string is formed by reversing the string and then taking the complement of each nucleotide.

A few examples of reverse complements are shown below:

| Sample Sequence | Complement   | Reverse Complement |
|-----------------|--------------|--------------------|
| ATGATCTCGTAA    | TACTAGAGCATT | TTACGAGATCAT       |
| GCTAGCTAGCTA    | CGATCGATCGAT | TAGCTAGCTAGC       |

## Task
1. Create an activity diagram that describes the steps to reverse complement a DNA sequence.
2. Clone this repository and set up a virtual environment.
3. Implement a python module `reverse_complement.py` that provides a function `reverse_complement` that takes a DNA string as input and returns the reverse complement of the DNA string.
   - To aid in the implementation and subsequent testing a unit test module `test_reverse_complement.py` is provided in this repository
   - In order to run all unit tests in the `test` directory run the following command:
     ```sh
     python -m unittest discover test
     ```
   - All the test cases in the test module should pass
4. The implementation should now be made error proof by substituting any non-DNA characters with an underscore character `"_"` in the output.
   - This change should be first developed in a new branch `error_resistent` and then merged back into the `main` branch.
   - Before making the changes to the function adapt the activity diagram to include the new steps.
   - Update the test module to include the new test case by adding a function `test_reverse_complement_error_resistent` to the `TestReverseComplement` class.  
   This test case should verify that the DNA string `"ATGATCTCXTAA"` returns the reverse complement `"TTACGAGA_CAT"`.
   - Once again all the test cases should pass after the implementation.
5. Try to assess whether the implementation is efficient and easily extendable and suggest any improvements if necessary.