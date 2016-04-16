# /* Iteration for max subarray   Version 2

# 	don't compute sums from scratch
# 	the sum of elements from k to j, can also help to compute
# 	the sum of elements from k to j + (j+1)
# 	Same as enumeration, but cleverly done so.

# 	function maxsubarray(a[1, ... ,n])
# 		for i = i, ..., n
# 		sum = 0
# 		for j = i, ..., n
# 			sum = sum + a[j]
# 			keep max sum found so far
# 	return max sum found



# 	analysis O(n) i-iterations x O(n) j-iterations x O(1) time to update sum = O(n^2)



# */


def brute_forceV2(array):
    max = 0
    size = len(array)

    for minIndex in range(0, size - 1):
        for index in range(minIndex+1, size):
            sum += array[index]

            if (sum > max):
                max = sum
    return max


myList = [-5, 10, -100, 3, -100, 5, -9]


greatest_number = brute_forceV2(myList)
print("The max of this array is:", greatest_number)
