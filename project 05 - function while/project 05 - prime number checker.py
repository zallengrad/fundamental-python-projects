def prime_checker(number):
    if number < 2:
        print(f"It's not a prime number.")
        return

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"It's not a prime number.")
            return

    print(f"It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
