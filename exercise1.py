def check_letter():
    letter = input("Enter a letter: ")

    if not letter.isalpha() or len(letter) != 1:
        print("Invalid input.")
    else:
        letter = letter.lower()
        if letter in "aeiou":
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")

check_letter()