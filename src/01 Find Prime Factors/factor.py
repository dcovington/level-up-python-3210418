def get_prime_factors(number):
    factorsx = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factorsx.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factorsx


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
