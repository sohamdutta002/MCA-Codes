# character_frequency_count

def character_frequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

string = "abcdefgabc"
frequency = character_frequency(string)
for char, count in frequency.items():
    print(f"{char},{count}")
