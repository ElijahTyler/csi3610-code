def sieve(n):
    prime_bools = [True] * n # write all numbers up to n
    primes = []
    root_bound = int(n**0.5)
    for i in range(2, n):
        if prime_bools[i]:
            primes.append(i)
            if i < root_bound:
                multiple = 2
                while i*multiple < n:
                    prime_bools[i*multiple] = False # crossing off the multiples
                    multiple += 1
    return primes

assert sieve(1000)[99] == 541

sieve_list = sieve(15485864)
sieve_sum = sum(sieve_list)
print(f"sum of the first 1,000,000 prime numbers: {sieve_sum:,}")