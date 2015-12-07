def is_prime(number):
    """Returns true if number is prime
    """
    for element in range(number):
        if number % element == 0:
            return False
            
        return True
        
def print_next_prime(number):
    """Print the closest prime number larger than the prime lnumber in question
    """
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)