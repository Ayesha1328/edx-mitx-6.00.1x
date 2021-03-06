# lec6.2-divisors.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 56, video 2

def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    total += d
print(total)


# Example calls to findDivisors
findDivisors(20, 100)
