def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Invalid age.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

    except ValueError:
        print("Please enter a valid number.")

check_voting_eligibility()