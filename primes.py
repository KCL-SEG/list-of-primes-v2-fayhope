def primes(number_of_primes):
    list = []
    x = 2
    if number_of_primes > 0 and isinstance(number_of_primes, int):
        while len(list) is not number_of_primes:
            midpoint = x//2
            prime = True 
            for y in range(2,midpoint+1):
                if x%y == 0:
                    prime = False
            if prime:
                list.append(x)
            x += 1
            print(list)
    else:
        raise ValueError
    return list
