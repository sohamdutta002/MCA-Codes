# string_manipulations

def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    return string == reverse_string(string)

def ends_with(string, substring):
    return string.endswith(substring)

def capitalize_first_letter(string):
    return string.title()

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

# Example:
string = "madam"
print(f"Reversed string: {reverse_string(string)}")
print(f"Is palindrome: {is_palindrome(string)}")
print(f"Ends with 'am': {ends_with(string, 'am')}")
print(f"Capitalized: {capitalize_first_letter(string)}")
print(f"Is anagram (madam, damam): {is_anagram('madam', 'damam')}")
print(f"String without vowels: {remove_vowels('hello world')}")
print(f"Length of the longest word: {longest_word_length('practice makes perfect')}")
