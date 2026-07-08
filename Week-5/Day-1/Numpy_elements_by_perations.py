import numpy as np

# arr1  =  np. array ([1 ,  2 ,  3])
# arr2  =  np. array ([4 ,  5 ,  6])
# sum_arr  = arr1  +  arr2	

# arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
# bool_idx  =  arr  >  3
# print (arr[ bool_idx])


# arr5=np.array([1,2,3,4,5,6,7,8,9])	
# print(np.percentile(arr5,50))
# print(np.quantile(arr5, 0.25))

# arr1  =  np. array ([1 ,  2 ,  3])
# arr2  =  np. array ([4 ,  5 ,  6])
# correlation  =  np. corrcoef( arr1 ,  arr2 )
# print(correlation)

# import numpy as np

# # 1. Generate matrix
# arr = (np.arange(1, 21) ** 2 + 1).reshape(4, 5)

# print("Original Matrix:")
# print(arr)

# # 2. Double the matrix
# double_arr = arr * 2

# print("\nDouble Matrix:")
# print(double_arr)

# # 3. Replace values divisible by 5 with -1
# new_arr = arr.copy()
# new_arr[new_arr % 5 == 0] = -1

# print("\nModified Matrix:")
# print(new_arr)

# # 4. Count replaced values
# count = np.sum(arr % 5 == 0)

# print("\nNumbers Replaced:", count)


# import numpy as np

# A = np.arange(1, 101).reshape(10, 10)
# print(A)


import numpy as np

# Generate random numbers
np.random.seed(42)
A = np.random.randint(1, 501, 1000)

# 1. Count perfect squares
count_square = np.sum(np.sqrt(A) == np.sqrt(A).astype(int))
print("Perfect Squares:", count_square)

# 2. Count prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_count = np.sum(np.vectorize(is_prime)(A))
print("Prime Numbers:", prime_count)

# 3. Replace multiples of 7 with square root
B = A.astype(float)
B[B % 7 == 0] = np.sqrt(B[B % 7 == 0])
print("\nModified Array:")
print(B)

# 4. Largest gap
sorted_A = np.sort(A)
largest_gap = np.max(np.diff(sorted_A))
print("\nLargest Gap:", largest_gap)

# 5. Cumulative sum
cum_sum = np.cumsum(A)
print("\nCumulative Sum:")
print(cum_sum)

# 6. First index where cumulative sum exceeds 100000
index = np.argmax(cum_sum > 100000)
print("\nFirst Index:", index)