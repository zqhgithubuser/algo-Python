import sys
from array import array

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
print(sys.getsizeof(primes_list))  # 120

primes_array = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print(sys.getsizeof(primes_array))  # 112
