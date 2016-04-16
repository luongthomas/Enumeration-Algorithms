# # Enumeration for max subarray

# 	function maxsubarray(a[1, ... ,n])
# 		for each pair (i, j) with 1 <= i < j <= n
# 		compute a[i] + a[i+1] + ... + a[j-1] + a[j]
# 		keep max sum found so far
# 	return max sum found



# analysis O(n^2) pairs x O(n) times to compute each sum = O(n^3)



def brute_force(array):
    max = 0
    size = len(array)

    for minIndex in range(0, size - 1):
        sum = 0
        for maxIndex in range(minIndex+1, size):

            # this loop sums up all the values for every single pair (inefficient)
            # adding 1 to maxindex, since range() doesn't include the last element.
            for index in range(minIndex, maxIndex+1):
                sum += array[index]

                if (sum > max):
                    max = sum
    return max


myList = [-5, 10, -100, 3, -100, 5, -9]


greatest_number = brute_force(myList)
print("The max of this array is:", greatest_number)
