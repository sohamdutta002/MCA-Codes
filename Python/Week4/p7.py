# words_composed_of_digits

def find_digit_words(sentence):
    words = sentence.split()
    digit_words = [word for word in words if word.isdigit()]
    return digit_words

sentence = "2 cats and 3 dogs."
digit_words = find_digit_words(sentence)
print(f"Words composed of digits: {digit_words}")
