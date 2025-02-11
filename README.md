# Tip Calculator

A simple, interactive Python program that calculates the amount each person should pay when splitting a bill, including tip.

## Description

The Tip Calculator helps users:
- Calculate the total bill including tip
- Split the bill among multiple people
- Handle different tip percentages (10%, 12%, or 15%)
- Get precise per-person amounts with 2 decimal places

## Features

- User-friendly interface
- Error handling for invalid inputs
- Continuous operation with exit option
- Precise decimal calculations
- Clear formatting of monetary amounts

## Prerequisites

To run this program, you need:
- Python 3.x installed on your system

## Installation

1. Save the code as `tip_calculator.py`
2. No additional packages or dependencies required

## Usage

1. Open your terminal/command prompt
2. Navigate to the directory containing `tip_calculator.py`
3. Run the program:
   ```bash
   python tip_calculator.py
   ```

### Input Format
1. Total Bill:
   - Enter the bill amount in dollars
   - Example: `45.50`

2. Tip Percentage:
   - Choose between 10, 12, or 15
   - Enter the number without the % symbol
   - Example: `12`

3. Number of People:
   - Enter a whole number
   - Example: `4`

### Example Session
```
Welcome to the Tip Calculator
What was the total bill? $100
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 4
Each person should pay: $28.00

Do you want to exit? Type 'e' to exit or press Enter to continue:
```

## Features in Detail

### Error Handling
- Catches invalid inputs (letters, special characters)
- Provides clear error messages
- Allows users to try again without restarting

### Calculation Method
1. Calculates tip amount: `bill * (tip_percentage / 100)`
2. Adds tip to original bill: `bill + tip_amount`
3. Divides total by number of people
4. Rounds result to 2 decimal places

### Program Flow
1. Welcomes user
2. Collects inputs
3. Performs calculations
4. Displays results
5. Offers to continue or exit

## Common Issues and Solutions

1. Invalid Input Errors:
   - Enter numbers only
   - Don't include currency symbols
   - Use dots (.) not commas (,) for decimals

2. Division Issues:
   - Number of people must be at least 1
   - Enter whole numbers only for people count

## Customization

You can modify the code to:
- Add more tip percentage options
- Change the decimal precision
- Modify the error messages
- Add currency selection
- Include additional calculations (e.g., tip amount per person)

## Best Practices for Use

1. Enter bill amount in decimal format (45.50, not 45,50)
2. Use whole numbers for people count
3. Select from suggested tip percentages
4. Review output before accepting results

## Contributing

Feel free to suggest improvements or modifications:
- Additional features
- UI enhancements
- More calculation options
- Better error handling

## Educational Value

This program demonstrates:
- Input/output operations
- Error handling with try/except
- String formatting
- Basic arithmetic operations
- User interface design
- Loop control
- Type conversion

## Version History

- 1.0: Initial release with basic functionality
- Future updates may include:
  - GUI interface
  - Additional tip options
  - Currency selection
  - Bill itemization

## License

Free to use for educational and personal purposes.
