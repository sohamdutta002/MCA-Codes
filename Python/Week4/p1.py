# string_length_substring_word_count.py

def string_analysis(sentence):
    # Calculate the length of the string
    length = len(sentence)
    
    # Find the substring 'country'
    substring_index = sentence.find('country')
    
    # Count occurrences of each word
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.strip('.,')  # Remove punctuation
        word_count[word] = word_count.get(word, 0) + 1
    
    return length, substring_index, word_count

sentence = "India is my motherland. I love my country. Capital of India is New Delhi."
length, substring_index, word_count = string_analysis(sentence)
print(f"Length of the string: {length}")
print(f"Index of 'country': {substring_index}")
print("Word count:", word_count)
