#8
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input())
    if number > 0:
        result = is_prime(number)
        if result:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
