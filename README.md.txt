# Pattern Generator and Number Analyzer

## Project Overview

This is a beginner-friendly Python project that combines two useful programs: Pattern Generator and Number Analyzer. It uses functions, loops, conditional statements, exception handling, and user input to perform different tasks.

## Features

1. **Pattern Generator:** Generates a right-angled triangle star pattern based on the number of rows entered by the user.
2. **Number Analyzer:** Analyzes a range of numbers and identifies whether each number is Even or Odd.
3. **Sum Calculator:** Calculates the sum of all numbers within the given range.
4. **Input Validation:** Handles invalid inputs and prevents negative or zero rows.
5. **Menu-Driven Program:** Allows users to select options and exit the program.

## Technologies Used

- Python 3
- Functions
- While Loop
- For Loop
- If-Else Statements
- Try-Except (Exception Handling)
- User Input and Type Casting

## Project Logic

### 1. Pattern Generator (`pattern_generator()`)
- Takes the number of rows from the user.
- Validates that the input is a positive integer.
- Uses nested for loops to print a star pattern.

### 2. Number Analyzer (`number_analyzer()`)
- Takes start and end values from the user.
- Validates the range.
- Uses a for loop to check each number.
- Uses the modulo operator (%) to identify Even and Odd numbers.
- Calculates the total sum of the range.

### 3. Main Function (`main()`)
- Displays the main menu.
- Takes the user's choice.
- Calls the selected function.
- Repeats until the user chooses Exit.

## How to Run the Project

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in CMD or Terminal.
4. Run the following command:

```bash
python main.py
```

## Sample Output

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 1
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****

Select an option:
2
Enter the start of the range: 1
Enter the end of the range: 5
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
Sum of all numbers from 1 to 5 is: 15

Select an option:
3
Exiting the program. Goodbye!
```

## Learning Outcomes

Through this project, I learned how to:
- Create and call Python functions.
- Use nested loops to generate patterns.
- Apply conditional statements.
- Handle invalid user inputs using try-except.
- Analyze numbers using the modulo operator.
- Calculate the sum of a numerical range.
- Build a menu-driven Python application.

## Author

Created as a Python programming practice project.