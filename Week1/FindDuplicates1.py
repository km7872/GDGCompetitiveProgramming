from typing import List

"""
Given a string s and an integer k, return a list of characters in the string s that appear more than k times. You may assume that the input string only contains lowercase English letters.
"""

def find_duplicates(s: str, k: int) -> List[str]:
    """
        This function finds all characters in the string `s` that appear more than `k` times.

        Parameters:
        s (str): The input string.
        k (int): The threshold for occurrences.

        Returns:
        List[str]: A list of characters that appear more than `k` times.
    """
    pass
    # code goes here :)



# Test case 1: Basic case with multiple characters having counts greater than k
print(find_duplicates("abcaabcc", 2))
# Expected Output: ['a', 'c']
# Explanation: 'a' appears 3 times and 'c' appears 3 times, both more than 2 times.

# Test case 2: No characters appear more than k times
print(find_duplicates("abcdefg", 1))
# Expected Output: []
# Explanation: All characters appear only once, so no character appears more than 1 time.

# Test case 3: A character appears more than k times in a long string
long_string = "a" * 1000 + "b" * 500 + "c" * 200 + "d" * 100
print(find_duplicates(long_string, 100))
# Expected Output: ['a', 'b']
# Explanation: 'a' appears 1000 times and 'b' appears 500 times, both more than 100 times.

# Test case 4: Only one character in the string
long_string = "a" * 1000
print(find_duplicates(long_string, 100))
# Expected Output: ['a']
# Explanation: 'a' appears 1000 times, so it's the only character that appears more than 100 times.

# Test case 5: All characters appear the same number of times
long_string = "ababababab" * 100
print(find_duplicates(long_string, 5))
# Expected Output: ['a', 'b']
# Explanation: 'a' and 'b' both appear 500 times, which is more than 5.

# Test case 6: Case with multiple characters, some appear more than k times
long_string = "abccbaabcabcabcabca" * 100
print(find_duplicates(long_string, 10))
# Expected Output: ['a', 'b', 'c']
# Explanation: 'a', 'b', and 'c' appear more than 10 times each in the string.

# Test case 7: Edge case with k = 0, everything should be considered as duplicate
long_string = "a" * 1000 + "b" * 500 + "c" * 200
print(find_duplicates(long_string, 0))
# Expected Output: ['a', 'b', 'c']
# Explanation: Since k=0, any character that appears more than once should be returned.

# Test case 8: Large input case with repeated sequences
long_string = ("a" * 500 + "b" * 300 + "c" * 200) * 50
print(find_duplicates(long_string, 300))
# Expected Output: ['a', 'b']
# Explanation: 'a' appears 500 times, and 'b' appears 300 times, both more than 300.

# Test case 9: Edge case with an empty string
print(find_duplicates("", 1))
# Expected Output: []
# Explanation: There are no characters in the string, so no duplicates.

# Test case 10: Case with no characters appearing more than k times
long_string = "abcdefghij" * 100
print(find_duplicates(long_string, 1))
# Expected Output: []
# Explanation: All characters appear only once, so no character appears more than 1 time.
