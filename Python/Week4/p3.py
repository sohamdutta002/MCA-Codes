# capitalize_lines

def capitalize_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to stop): ")
        if line:
            lines.append(line.upper())
        else:
            break
    return lines

capitalized_lines = capitalize_lines()
for line in capitalized_lines:
    print(line)
