class PalindromicSubsequenceCounter:
    def __init__(self, s: str):
        self.s = s
        self.n = len(s)

    def validate_input(self):
        if not (1 < self.n < 10):
            raise ValueError("String length must be between 2 and 9")

    def is_palindrome(self, text: str) -> bool:
        return text == text[::-1]

    def generate_subsequences(self):
        subsequences = []
        for mask in range(1, 1 << self.n):
            subseq = ""
            for i in range(self.n):
                if mask & (1 << i):
                    subseq += self.s[i]
            subsequences.append(subseq)
        return subsequences
#--------------2---------------    

    def count_distinct_palindromic_subsequences(self) -> int:
        self.validate_input()
        palindromes = set()

        for subseq in self.generate_subsequences():
            if self.is_palindrome(subseq):
                palindromes.add(subseq)

        return len(palindromes)

    def display_palindromes(self):
        palindromes = set()
        for subseq in self.generate_subsequences():
            if self.is_palindrome(subseq):
                palindromes.add(subseq)

        print("\nDistinct Palindromic Subsequences:")
        for p in sorted(palindromes):
            print(p)
#---------------3----------------            


# -------- Main Program --------
try:
    s = input("Enter a string: ")
    counter = PalindromicSubsequenceCounter(s)
    result = counter.count_distinct_palindromic_subsequences()

    print("\nTotal number of distinct palindromic subsequences:", result)
    counter.display_palindromes()

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)