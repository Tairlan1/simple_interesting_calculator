# calculator.py
# Interest = Principal × Rate × Time
# Rate is a decimal, e.g., 5% = 0.05, and Time is in years
def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest


if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        time = float(input("Enter the time period in years: "))

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print(f"\nSimple Interest: {interest:.2f}")
        print(f"Total Amount: {total_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")