# count_letters_and_digits

def count_letters_and_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return letters, digits

sentence = "hello world! 123"
letters, digits = count_letters_and_digits(sentence)
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
