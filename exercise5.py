def determine_season():
    month = input("Enter the month (Jan - Dec): ").capitalize()

    try:
        day = int(input("Enter the day of the month: "))
    except ValueError:
        print("Invalid day.")
        return

    if month == "Dec":
        if day >= 21:
            season = "Winter"
        else:
            season = "Fall"

    elif month in ["Jan", "Feb"]:
        season = "Winter"

    elif month == "Mar":
        if day >= 20:
            season = "Spring"
        else:
            season = "Winter"

    elif month in ["Apr", "May"]:
        season = "Spring"

    elif month == "Jun":
        if day >= 21:
            season = "Summer"
        else:
            season = "Spring"

    elif month in ["Jul", "Aug"]:
        season = "Summer"

    elif month == "Sep":
        if day >= 22:
            season = "Fall"
        else:
            season = "Summer"

    elif month in ["Oct", "Nov"]:
        season = "Fall"

    else:
        print("Invalid month.")
        return

    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()