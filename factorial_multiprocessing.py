import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

#func to compute fact for a given number

def factorial(number):
    print(f"Computing the factorial of {number}:")
    result = math.factorial(number)
    print(f"fcatorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers= [4000,5000,6000,7000]

    start_time = time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial,numbers)

    end_time = time.time()

    print(f"Results : {results}")
    print(f"Time taken : {end_time-start_time} seconds")