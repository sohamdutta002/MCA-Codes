# sort_words_alphabetically

def sort_words(sequence):
    words = sequence.split(',')
    words.sort()
    return ','.join(words)

sequence = "without,hello,bag,world"
sorted_sequence = sort_words(sequence)
print(f"Sorted words: {sorted_sequence}")
