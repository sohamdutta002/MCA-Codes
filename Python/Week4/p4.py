# remove_duplicates_and_sort

def remove_duplicates_and_sort(sequence):
    words = sequence.split()
    unique_words = sorted(set(words))
    return ' '.join(unique_words)

sequence = "hello world and practice makes perfect and hello world again"
result = remove_duplicates_and_sort(sequence)
print(f"Result: {result}")
