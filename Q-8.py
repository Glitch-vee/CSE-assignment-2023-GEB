class SumOfDigits:
    def __init__(self, number):
        self.number = number

    def sum_of_digits(self):
        digit_list = [int(d) for d in str(self.number)]
        return sum(digit_list)

def main():
    number = int(input("Enter a positive integer: "))
    if number > 0:
        obj = SumOfDigits(number)
        print("Sum of digits of", number, "is", obj.sum_of_digits())
    else:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
