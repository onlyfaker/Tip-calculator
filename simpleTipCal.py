while True:
    print("Welcome to the Tip Calculator")
    try:
        bill = float(input("What was the total bill? $"))
        tip = float(input("How much tip would you like to give? 10, 12, or 15? %"))
        num_of_people = int(input("How many people to split the bill? "))
        final_bill = bill + (bill * tip) / 100
        amount_per_person = final_bill / num_of_people
        print(f"Each person should pay: ${amount_per_person:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

    user_input = input("Do you want to exit? Type 'e' to exit or press Enter to continue: ")
    if user_input.lower() == "e":
        break
