number = input("Enter a number: ") # we take a number from the user
digitNumber = len(number) # we find the length of the number
amstrongNumber = int(number) # we convert the number to an integer
sumNumber = 0 # we initialize the sum of the number
for i in number: # we iterate through the number
    sumNumber += int(i) ** digitNumber # we calculate the sum of the number
if amstrongNumber == sumNumber: # we check if the number is an Armstrong number
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#################################
# Second way
def is_armstrong_number(number):
    digit_number = len(number)
    sum_number = sum(int(i) ** digit_number for i in number)  # List comprehension 
    return int(number) == sum_number
if __name__ == "__main__":
    number = input("Enter a number: ") 
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

