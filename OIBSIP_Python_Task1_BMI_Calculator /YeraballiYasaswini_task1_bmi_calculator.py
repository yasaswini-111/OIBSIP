print("=" * 50)
print("        BMI HEALTH CALCULATOR")
print("=" * 50)

while True:

    # Name Validation
    while True:
        name = input("\nEnter your name: ").strip()

        if name.replace(" ", "").isalpha():
            break
        else:
            print("Please enter a valid name using alphabets only.")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("\nWeight and height must be greater than zero.")
            continue

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            tip = "Eat a healthy and balanced diet."
        elif bmi < 25:
            category = "Normal Weight"
            tip = "Great! Keep maintaining your healthy lifestyle."
        elif bmi < 30:
            category = "Overweight"
            tip = "Exercise regularly and reduce junk food."
        else:
            category = "Obese"
            tip = "Consult a healthcare professional for guidance."

        ideal_min = round(18.5 * (height ** 2), 2)
        ideal_max = round(24.9 * (height ** 2), 2)

        print("\n" + "-" * 45)
        print("              BMI REPORT")
        print("-" * 45)
        print(f"Name          : {name.title()}")
        print(f"Weight        : {weight} kg")
        print(f"Height        : {height} m")
        print(f"BMI           : {bmi}")
        print(f"Category      : {category}")
        print(f"Health Tip    : {tip}")
        print(f"Ideal Weight  : {ideal_min} kg - {ideal_max} kg")
        print("-" * 45)

    except ValueError:
        print("\nPlease enter valid numeric values only.")

    while True:
        choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()

        if choice in ["yes", "y"]:
            break
        elif choice in ["no", "n"]:
            print("\nThank you for using BMI Health Calculator.")
            print("Stay Healthy!")
            exit()
        else:
            print("Please enter only 'yes' or 'no'.")
