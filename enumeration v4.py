# /* Recursion Inversion for max subarray

# 	the max subarray either uses the last element or doesn't:

# 		MAXSUBARRAY(a[1,..., n]) = max  {MAXSUBARRAY(a[1, ..., n-1]),
# 										{MAXSUFFIX(a[1,...,n])
# 		MAXSUFFIX(a[1,..., n]) = max {MAX(0, a[1, ..., n-1]) + a[n] }

# 	dynamic programming 	evaluate this non-recursively by computing

# 	1. first MAXSUBARRAY(a[1]) and MAXSUFFIX(a[1])
# 	2. then MAXSUBARRAY(a[1,2]) and MAXSUFFIX(a[1,2] from above
# 	3. then MAXSUBARRAY(a[1,2,3]) and MAXSUFFIX(a[1,2,3] from above
# 	4. and so on

	

# 	analysis computing MAXSUBARRAY(a[1,..., n]) and  MAXSUFFIX(a[1, ..., n])
# 		from MAXSUBARRAY(a[1,..., n-1]) and  MAXSUFFIX(a[1, ..., n-1])
# 			takes O(1) time

# 	O(n) things to compute = O(n) time



#  pseudocode from lecture
# 	MAX_SUB_ARRAY_LINEAR(A)
# 		n = A.length
# 		maxsum = -infinity
# 		for j = 1 to n
# 			endingHereHigh = j
# 			if endingHereSum > 0
# 				endingHereSum = endingHereSum + A[j]
# 			else endingHereLow = j
# 				endingHereSum = A[j]
# 			if endingHereSum > maxSum
# 				maxSum = endingHereSum
# 				low = endingHereLow
# 				high = endingHereHigh
# 		return(low, high, max-sum)



		





# */
import time
import sys
import string

#############################################
# Read file and generate array of number array
#
# @pram filename : filename read
#############################################
def read_file(filename):
    numbers = []
    for l in open(param[1]).readlines():
    	if (']' in l) == False:
            continue
        l=l.translate(string.maketrans("", ""), "[] ")
        l=l.replace(" ", "")
        data = l[:-1].split(',')
        x= []
        for n in data:
            x += [int(n)]
        numbers.append(x)
    return numbers

#############################################
# convert array to writable format of array
#
# @param array : the array converted
#############################################
def convert_int_array(array):
    str_arr = "["
    for idx, n in enumerate(array):
        if idx != 0:
            str_arr += ","
        str_arr += str(n)
    str_arr += "]"
    return str_arr

# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Kadane's algorithm
def max_subarray(array):
    t_start = time.clock()
    max_ending_here = max_so_far = 0
    max_from = max_to = 0
    start = 0
    for idx, x in enumerate(array):
        if max_ending_here == 0:
            start = idx
        max_ending_here = max(0, max_ending_here + x)
        if max_so_far < max_ending_here:
            max_from = start
            max_to = idx
        max_so_far = max(max_so_far, max_ending_here)
    t_end = time.clock()
    print ("DP finished in time: %8.8f" %(t_end - t_start))

    return array[max_from:max_to+1]



param = sys.argv
if len(param) < 3:
    print "Give input filename and output filename"
    exit(-1)

numbers = read_file(param[1])

print numbers
print "\n"

out = open(param[2], "wt")

for idx, arr in enumerate(numbers):
    sub_array = max_subarray(arr)
    greatest_number = 0
    for n in sub_array:
        greatest_number += n
    s = "[DP]The max of this array is:" + str(greatest_number)
    print s
    print arr
    print sub_array
    print "\n"
    if idx != 0:
        out.write("\n")
    out.write(convert_int_array(arr) + "\n")
    out.write(convert_int_array(sub_array) + "\n")
    out.write(str(greatest_number) + "\n")
out.close()














