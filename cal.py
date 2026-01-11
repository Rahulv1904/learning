import math
from datetime import datetime

# ---------- Calculator Class ----------
class AdvancedCalculator:
    def __init__(self):
        self.history = []

    # ---------- Basic Operations ----------
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b

    # ---------- Scientific Operations ----------
    def square_root(self, a):
        return math.sqrt(a)

    def log(self, a):
        return math.log10(a)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    # ---------- History ----------
    def save_history(self, expression, result):
        self.history.append(
            f"{datetime.now().strftime('%H:%M:%S')} | {expression} = {result}"
        )

    def show_history(self):
        if not self.history:
            print("No history found.")
        else:
            print("\n--- Calculation History ---")
            for item in self.history:
                print(item)

# ---------- Main Program ----------
def main():
    calc = AdvancedCalculator()

    while True:
        print("\n====== ADVANCED CALCULATOR ======")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Log (base 10)")
        print("9. Sin")
        print("10. Cos")
        print("11. Tan")
        print("12. Show History")
        print("13. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice in [1, 2, 3, 4, 5, 6]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    result = calc.add(a, b)
                    expr = f"{a} + {b}"
                elif choice == 2:
                    result = calc.subtract(a, b)
                    expr = f"{a} - {b}"
                elif choice == 3:
                    result = calc.multiply(a, b)
                    expr = f"{a} * {b}"
                elif choice == 4:
                    result = calc.divide(a, b)
                    expr = f"{a} / {b}"
                elif choice == 5:
                    result = calc.power(a, b)
                    expr = f"{a} ^ {b}"
                elif choice == 6:
                    result = calc.modulus(a, b)
                    expr = f"{a} % {b}"

            elif choice == 7:
                a = float(input("Enter number: "))
                result = calc.square_root(a)
                expr = f"√{a}"

            elif choice == 8:
                a = float(input("Enter number: "))
                result = calc.log(a)
                expr = f"log({a})"

            elif choice == 9:
                a = float(input("Enter angle in degrees: "))
                result = calc.sin(a)
                expr = f"sin({a})"

            elif choice == 10:
                a = float(input("Enter angle in degrees: "))
                result = calc.cos(a)
                expr = f"cos({a})"

            elif choice == 11:
                a = float(input("Enter angle in degrees: "))
                result = calc.tan(a)
                expr = f"tan({a})"

            elif choice == 12:
                calc.show_history()
                continue

            elif choice == 13:
                print("Thank you for using Advanced Calculator 🚀")
                break

            else:
                print("Invalid choice")
                continue

            print("Result:", result)
            calc.save_history(expr, result)

        except Exception as e:
            print("Error:", e)


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
