from src.miller_rabin import miller_rabin_test
from src.utils.msg import input_key, not_valid_input, prime, not_prime, good_by, exit_key

# Main input program
print(exit_key)
while True:
    try:
        num = int(input(input_key))
        if num == 0:
            print(good_by)
            break
        elif miller_rabin_test(n=num):
            print(prime.format(n=num))
        else:
            print(not_prime.format(n=num))
    except ValueError:
        print(not_valid_input)
