def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the division in the rang [2, P).
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)

# Запускаем код в режиме интерпретатора Python:
# from Lesson14.test_doctest_01 import is_prime
# is_prime(42)
# is_prime(73)
