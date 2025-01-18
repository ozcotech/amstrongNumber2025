# Armstrong Number Checker

This Python program checks whether a given number is an **Armstrong number**. An Armstrong number (also known as a narcissistic number) is a number that equals the sum of its own digits each raised to the power of the number of digits.

---

## **What is an Armstrong Number?**
A number is an Armstrong number if:
\[
\text{Sum of (each digit raised to the power of the number of digits)} = \text{Original number}
\]

### Examples:
1. **153**
   \[
   1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
   \]
   **153 is an Armstrong number.**

2. **9474**
   \[
   9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
   \]
   **9474 is an Armstrong number.**

3. **123**
   \[
   1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
   \]
   **123 is NOT an Armstrong number.**

---

## **How It Works**
This program provides **two different implementations** to check for Armstrong numbers:
1. A simple, inline solution using a `for` loop.
2. A modular and reusable function `is_armstrong_number()`.

---

## **Code Explanation**

## **🔴 First Implementation**
The first method directly calculates whether the input number is an Armstrong number:
```python
number = input("Enter a number: ")  # Get input from the user
digitNumber = len(number)           # Count the number of digits
amstrongNumber = int(number)        # Convert the input to an integer
sumNumber = 0                       # Initialize sum

# Iterate through each digit of the number
for i in number:
    sumNumber += int(i) ** digitNumber  # Add the power of the digit to the sum

# Check if the number is an Armstrong number
if amstrongNumber == sumNumber:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
----

## **🔴 Second Implementation**

def is_armstrong_number(number):
    """Check if a number is an Armstrong number."""
    digit_number = len(number)
    sum_number = sum(int(i) ** digit_number for i in number)  # Sum of powers
    return int(number) == sum_number

if __name__ == "__main__":
    number = input("Enter a number: ")  # Get input from the user
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")