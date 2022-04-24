def isComposite(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def unique_prime_factors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

abcabc = []

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            n = k + j*10 + i*100 + k*1000 + j*10000 + i*100000
            factors = unique_prime_factors(n)
            if len(factors) > 1:
                unique_factors = list(dict.fromkeys(factors))
                if len(factors) == len(unique_factors):
                    goodCarmichael = True
                    for num in unique_factors:
                        if (n - 1) % (num - 1) != 0:
                            goodCarmichael = False
                            break
                    if goodCarmichael:
                        abcabc.append(n)

print(abcabc)
