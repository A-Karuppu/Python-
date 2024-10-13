def generate_primes():
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

generate_primes()
