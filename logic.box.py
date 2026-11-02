def pattern_generator():
    while True:
        try:
            rows = int(input("Enter the number of rows for the pattern: "))
            if rows > 0:
                break
            else:
                print("Error: Please enter a positive integer for rows.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
            
    print("\nPattern:")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
    print()

def number_analyzer():
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            
            if end >= start:
                break
            else:
                print("Error: The end of the range must be greater than or equal to the start.")
        except ValueError:
            print("Error: Invalid input. Please enter valid integers.")
            
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
        total_sum += num
        
    print(f"Sum of all numbers from {start} to {end} is: {total_sum}\n")

def main():
    print("Welcome to the Pattern Generator and Number Analyzer!")
    
    while True:
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pattern_generator()
        elif choice == '2':
            number_analyzer()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
