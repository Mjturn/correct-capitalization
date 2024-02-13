def is_correct_capitalization(string):
    remove_first_letter = string[1:]

    if string[0].isupper():
        if remove_first_letter.isupper():
            return True
        elif remove_first_letter.islower():
            return True
    else:
        if remove_first_letter.islower():
            return True
        else:
            return False

inputs = ["USA", "Calvin", "compUter", "coding"]

for input in inputs:
    print(is_correct_capitalization(input))
