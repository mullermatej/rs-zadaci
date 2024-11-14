def isPrime(broj):
    uvjet = 0
    for i in range(broj):
        i += 1
        if (broj % i == 0):
            uvjet += 1
    if (uvjet == 2):
        return True
    else:
        return False


def primes_in_range(start, end):
    prosti_brojevi = []
    uvjet = 0
    for i in range(start, end):
        for k in range(i):
            k += 1
            if (i % k == 0):
                uvjet += 1
        if (uvjet == 2):
            prosti_brojevi.append(i)
            uvjet = 0
        else:
            uvjet = 0
    return prosti_brojevi


print(isPrime(7))  # True
print(isPrime(10))  # False
print(primes_in_range(1, 10))  # [2, 3, 5, 7]
