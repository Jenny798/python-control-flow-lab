def calculate_dog_years():
    try:
        age = int(input("Enter dog's age: "))

        if age < 0:
            print("Invalid age.")
        elif age <= 2:
            dog_years = age * 10
        else:
            dog_years = 20 + (age - 2) * 7

        print(f"Dog's age in dog years is {dog_years}")

    except ValueError:
        print("Enter a valid number.")

calculate_dog_years()