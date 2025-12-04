# ---------------------------------------------------------------
# Gross Pay and Tax Deduction Calculator
# Author: Your Name
# Description:
#   Part 1: Calculate gross pay using hourly rate and hours worked.
#   Part 2: Deduct tax using NZ income tax brackets.
# ---------------------------------------------------------------

def calculate_gross_pay(hourly_rate, hours_worked):
    """
    Calculate gross pay by multiplying rate × hours.
    """
    return hourly_rate * hours_worked


def calculate_tax(income):
    """
    Calculate tax based on New Zealand tax brackets (2024–2025).
    Source: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
    """

    # NZ individual income tax rates
    brackets = [
        (15600, 0.105),       # 10.5% on income up to $14,000
        (53500, 0.175),       # 17.5% on income from $14,001 to $48,000
        (78100, 0.30),        # 30% on income from $48,001 to $70,000
        (180000, 0.33),       # 33% on income from $70,001 to $180,000
        (float("inf"), 0.39)  # 39% on income over $180,000
    ]

    tax_total = 0
    previous_limit = 0

    # Calculate progressive tax
    for limit, rate in brackets:
        if income > previous_limit:
            # Taxable income within the current bracket
            taxable_amount = min(income, limit) - previous_limit
            tax_total += taxable_amount * rate
            previous_limit = limit
        else:
            break

    return tax_total


def main():
    """
    Main function to run the program.
    """

    print("=== Gross Pay & Tax Calculator ===")

    # ---- Part 1 Inputs ----
    # Ask user for hourly pay rate
    hourly_rate = float(input("Enter your hourly rate ($): "))

    # Ask user for number of hours worked
    hours_worked = float(input("Enter hours worked: "))

    # Calculate gross pay
    gross_pay = calculate_gross_pay(hourly_rate, hours_worked)
    print(f"\nGross Pay: ${gross_pay:.2f}")

    # ---- Part 2 Tax Calculation ----
    tax_amount = calculate_tax(gross_pay)
    final_income = gross_pay - tax_amount

    # Display final results
    print(f"Tax Deducted: ${tax_amount:.2f}")
    print(f"Final Take-Home Income: ${final_income:.2f}")


# Run the program only when executed directly
if __name__ == "__main__":
    main()
