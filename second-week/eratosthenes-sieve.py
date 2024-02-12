def eratosthenes_sieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            print(f"{num} είναι πρώτος.")
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
                print(f"Αφαίρεσε τα πολλαπλάσια του {num} από {multiple}.")
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
            print(f"{num} είναι πρώτος.")
    return primes

limit = 20
prime_numbers = eratosthenes_sieve(limit)
print("Οι πρώτοι αριθμοί μέχρι το", limit, "είναι:", prime_numbers)

