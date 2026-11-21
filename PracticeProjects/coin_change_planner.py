# Find the fewest coins needed for an amount, even for unusual denominations.
# Practice: dynamic programming, lists, reconstruction, and Counter.
from collections import Counter


def plan_change(amount, denominations):
    if type(amount) is not int or not 0 <= amount <= 10000:
        raise ValueError("Amount must be a whole number from 0 to 10000.")
    if not denominations or len(denominations) > 100:
        raise ValueError("Enter from 1 to 100 denominations.")
    if any(type(coin) is not int or not 1 <= coin <= 10000 for coin in denominations):
        raise ValueError("Denominations must be whole numbers from 1 to 10000.")
    coins = sorted(set(denominations))
    best = [amount + 1] * (amount + 1)
    chosen = [None] * (amount + 1)
    best[0] = 0
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin > subtotal:
                break
            if best[subtotal - coin] + 1 < best[subtotal]:
                best[subtotal] = best[subtotal - coin] + 1
                chosen[subtotal] = coin
    if chosen[amount] is None and amount != 0:
        raise ValueError("These denominations cannot make the requested amount.")
    counts = Counter()
    remaining = amount
    while remaining:
        coin = chosen[remaining]
        counts[coin] += 1
        remaining -= coin
    return dict(sorted(counts.items(), reverse=True))


def main():
    print("Coin Change Planner - amounts and denominations use whole units.")
    while True:
        text = input("Amount (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            amount = int(text)
            coins = [int(part) for part in input("Comma-separated denominations: ").split(",")]
            plan = plan_change(amount, coins)
            for coin, count in plan.items():
                print(f"{coin} x {count}")
            print(f"Minimum coins: {sum(plan.values())}")
        except ValueError as error:
            print(f"Cannot plan change: {error}")


if __name__ == "__main__":
    main()
