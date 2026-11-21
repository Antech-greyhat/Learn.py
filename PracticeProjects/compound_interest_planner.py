# Model yearly interest with a deposit added at the end of each year.
# Practice: Decimal, rounding, recurrence relations, and table output.
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext


def parse_decimal(text, maximum):
    if len(text) > 30:
        raise ValueError("Numeric input cannot exceed 30 characters.")
    try:
        value = Decimal(text.strip())
    except InvalidOperation as error:
        raise ValueError("Enter a numeric value.") from error
    if not value.is_finite() or not 0 <= value <= maximum:
        raise ValueError(f"Value must be finite and from 0 to {maximum}.")
    return value


def project_savings(principal_text, rate_text, years, deposit_text="0"):
    principal = parse_decimal(principal_text, Decimal("1000000"))
    rate = parse_decimal(rate_text, Decimal("100"))
    deposit = parse_decimal(deposit_text, Decimal("1000000"))
    if type(years) is not int or not 0 <= years <= 100:
        raise ValueError("Years must be a whole number from 0 to 100.")
    cent = Decimal("0.01")
    with localcontext() as context:
        context.prec = 80
        if principal != principal.quantize(cent) or deposit != deposit.quantize(cent):
            raise ValueError("Principal and yearly deposits must use whole cents.")
        balance = principal
        schedule = []
        for year in range(1, years + 1):
            interest = (balance * rate / 100).quantize(cent, rounding=ROUND_HALF_UP)
            balance += interest + deposit
            schedule.append({"year": year, "interest": interest, "balance": balance})
    return schedule


def main():
    print("Compound Interest Planner - fixed yearly rate; deposits follow interest each year.")
    print("This is a learning simulation; fees, taxes, and inflation are omitted.")
    while True:
        principal = input("Starting amount (q to quit): ").strip()
        if principal.lower() == "q":
            break
        try:
            rate = input("Annual interest percentage: ")
            years = int(input("Years (0-100): "))
            deposit = input("Deposit at each year end: ")
            schedule = project_savings(principal, rate, years, deposit)
            for entry in schedule:
                print(f"Year {entry['year']}: interest {entry['interest']:.2f} | balance {entry['balance']:.2f}")
            if not schedule:
                print(f"No elapsed years; balance: {Decimal(principal):.2f}")
        except ValueError as error:
            print(f"Invalid savings input: {error}")


if __name__ == "__main__":
    main()
