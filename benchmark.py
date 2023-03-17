import time
import torch


limit = 100000 #increase this to 100000000 to see the difference
mps_device = torch.device("mps") #cuda #cpu



def sieve_of_atkin(limit):
    P = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for x in range(5, int(limit ** 0.5) + 1):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False

    for p in range(5, limit):
        if sieve[p]:
            P.append(p)
    return P


def is_prime_batch_torch(numbers):
    numbers = numbers.to(torch.int32)
    max_number = torch.max(numbers).item()
    prime_flags = torch.ones_like(numbers, dtype=torch.bool)

    for i in range(2, int(torch.sqrt(torch.tensor(max_number)).item()) + 1):
        i = torch.tensor(i, device=numbers.device)
        non_primes = (numbers % i == 0) & (numbers != i)
        prime_flags &= ~non_primes

    prime_flags &= (numbers > 1)
    return prime_flags

def generate_safe_primes_torch(prime_numbers, device):
    numbers = torch.tensor(prime_numbers, device=device)
    safe_prime_flags = is_prime_batch_torch((numbers - 1) // 2)
    safe_primes = numbers[safe_prime_flags]

    return safe_primes.tolist()

if not torch.backends.mps.is_available():
    print("MPS not available on this system")
else:



    start_time = time.time()
    prime_numbers = sieve_of_atkin(limit)
    end_time = time.time()
    print(f"Sieve of Atkin took {end_time - start_time:.4f} seconds")

    start_time = time.time()
    safe_primes = generate_safe_primes_torch(prime_numbers, mps_device)
    end_time = time.time()
    print(f"Atkin Safe primes generation took {end_time - start_time:.4f} seconds")
    print(str(len(safe_primes) / limit))

    #print(safe_primes)










def is_prime_batch_torch(numbers):
    numbers = numbers.to(torch.int32)
    max_number = torch.max(numbers).item()
    prime_flags = torch.ones_like(numbers, dtype=torch.bool)

    for i in range(2, int(torch.sqrt(torch.tensor(max_number)).item()) + 1):
        i = torch.tensor(i, device=numbers.device)
        non_primes = (numbers % i == 0) & (numbers != i)
        prime_flags &= ~non_primes

    prime_flags &= (numbers > 1)
    return prime_flags


def is_prime_batch_torch(numbers):
    numbers = numbers.to(torch.int32)
    max_number = torch.max(numbers).item()
    prime_flags = torch.ones_like(numbers, dtype=torch.bool)

    for i in range(2, int(torch.sqrt(torch.tensor(max_number)).item()) + 1):
        i = torch.tensor(i, device=numbers.device)
        non_primes = (numbers % i == 0) & (numbers != i)
        prime_flags &= ~non_primes

    prime_flags &= (numbers > 1)
    return prime_flags

def sieve_of_eratosthenes_torch(limit, device):
    numbers = torch.arange(2, limit + 1, dtype=torch.int32, device=device)
    prime_flags = torch.ones_like(numbers, dtype=torch.bool)

    max_number = torch.max(numbers).item()
    for i in range(2, int(torch.sqrt(torch.tensor(max_number)).item()) + 1):
        i = torch.tensor(i, device=device)
        if prime_flags[i - 2]:
            non_primes = (numbers % i == 0) & (numbers != i)
            prime_flags &= ~non_primes

    return numbers[prime_flags]

def generate_safe_primes_torch(limit, device):
    prime_numbers = sieve_of_eratosthenes_torch(limit, device)
    safe_prime_flags = is_prime_batch_torch((prime_numbers - 1) // 2)
    safe_primes = prime_numbers[safe_prime_flags]

    return safe_primes.tolist()

if not torch.backends.mps.is_available():
    print("MPS not available on this system")
else:


    start_time = time.time()
    safe_primes = generate_safe_primes_torch(limit, mps_device)
    end_time = time.time()

    print(f"Erat Safe primes generation took {end_time - start_time:.4f} seconds")
    #print(safe_primes)
    print(str(len(safe_primes)/limit))


import torch

def is_prime_batch_torch(numbers):
    numbers = numbers.to(torch.int32)
    max_number = torch.max(numbers).item()
    prime_flags = torch.ones_like(numbers, dtype=torch.bool)

    for i in range(2, int(torch.sqrt(torch.tensor(max_number)).item()) + 1):
        i = torch.tensor(i, device=numbers.device)
        non_primes = (numbers % i == 0) & (numbers != i)
        prime_flags &= ~non_primes

    prime_flags &= (numbers > 1)
    return prime_flags


def generate_safe_primes_torch(limit, device):
    numbers = torch.arange(2, limit + 1, device=device)
    prime_flags = is_prime_batch_torch(numbers)
    prime_numbers = numbers[prime_flags]

    safe_prime_flags = is_prime_batch_torch((prime_numbers - 1) // 2)
    safe_primes = prime_numbers[safe_prime_flags]

    return safe_primes.tolist()

if not torch.backends.mps.is_available():
    print("MPS not available on this system")
else:


    start_time = time.time()
    safe_primes = generate_safe_primes_torch(limit, mps_device)

    end_time = time.time()
    print(f"Naive MPS Safe primes generation took {end_time - start_time:.4f} seconds")

    #Sprint(safe_primes)
    print(str(len(safe_primes)/limit))
    

