# yes_no_check

def yes_no_check(string):
    if string.lower() == "yes":
        return "Yes"
    else:
        return "No"

string = input("Enter a string: ")
print(yes_no_check(string))
