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
