def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a positive integer: "))
    if number > 0:
        result = is_prime(number)
        if result:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
    else:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
