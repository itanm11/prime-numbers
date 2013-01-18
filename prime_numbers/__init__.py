def is_prime_number(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i += 2
    return True

def get_prime_numbers(offset, limit):
    lst = []
    i = offset
    while (len(lst) < limit):
        if is_prime_number(i):
            lst.append(i)
        i = i + 1
    return lst
