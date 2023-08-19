from src.utils.Utils import Logger, gcd, power_mod, find_d_r
from src.utils.config import max_k
from src.utils import msg
import random


logger = Logger(__name__).get_logger()


def miller_rabin_test(n: int, k: int = max_k):

    # If n is equal to 1, then directly return False.
    if n <= 1:
        logger.info(msg.identity.format(n=n))
        return False

    # If n is equal to 2 or 3, then directly return True.
    if n <= 3:
        return True

    # If n is even, then directly return True.
    if n % 2 == 0:
        logger.info(msg.even.format(n=n))
        return False

    a_ = list()
    # Test that for a given random integer "a" on the range (2, n-2),
    # if greatest common divisor of a and n is different from 1, then n is not prime.
    a = random.randint(2, n-2)
    a_.append(a)
    gcd_a_n = gcd(a, n)
    if gcd_a_n != 1:
        logger.info(msg.gcd_a_n.format(a=a, n=n, gcd_a_n=gcd_a_n))
        logger.info(msg.list_a.format(a_=a_))
        return False

    # Find d and r such that n - 1 = d * 2^r
    d, r = find_d_r(n)

    # Perform the test k times
    for _ in range(k):

        # Get a random integer "a".
        a = random.randint(2, n-2)
        a_.append(a)

        # Solve for x = a^d (mod n)
        x = power_mod(a, d, n)

        # If the result is equal to 1 or n-1 continue testing.
        if x == 1 or x == n - 1:
            continue

        # If not, then make r-1 many loop so that at each step
        # update the problem x = x^2 (mod n) and check x is equal to n-1 or not.
        for _ in range(r - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            logger.info(msg.mr_test_not_prime.format(n=n))
            logger.info(msg.list_a.format(a_=a_))
            return False

    logger.info(msg.mr_test_prime.format(n=n))
    logger.info(msg.list_a.format(a_=a_))
    return True


if __name__ == "__main__":
    pass
