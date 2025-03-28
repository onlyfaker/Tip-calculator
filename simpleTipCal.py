while True:
    # Start of tip calculation session
    print("Welcome to the Tip Calculator")
    
    try:
        # Get bill details from user
        bill = float(input("What was the total bill? $"))
        tip = float(input("How much tip would you like to give? 10, 12, or 15? %"))
        num_of_people = int(input("How many people to split the bill? "))
        
        # Calculate total bill including tip
        final_bill = bill + (bill * tip) / 100
        
        # Split bill equally among people
        amount_per_person = final_bill / num_of_people
        
        # Display individual share with two decimal places
        print(f"Each person should pay: ${amount_per_person:.2f}\n")
    
    except ValueError:
        # Handle invalid numeric inputs
        print("Invalid input. Please enter numbers only.\n")
    
    # Option to continue or exit the calculator
    user_input = input("Do you want to exit? Type 'e' to exit or press Enter to continue: ")
    if user_input.lower() == "e":
        break
