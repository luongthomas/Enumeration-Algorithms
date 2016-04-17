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
    for l in open(filename).readlines():
        if ('[' in l) == False:
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


def brute_force(array):

    t_start = time.clock()
    max = 0
    max_from = max_to = 0
    size = len(array)

    for minIndex in range(0, size - 1):
        for maxIndex in range(minIndex+1, size):
            sum = 0

            # this loop sums up all the values for every single pair (inefficient)
            # adding 1 to maxindex, since range() doesn't include the last element.
            for index in range(minIndex, maxIndex+1):
                sum += array[index]

                if (sum > max):
                    max = sum
                    max_from = minIndex
                    max_to = index
    t_end = time.clock()
    print ("Better BF finished in time: %8.8f" %(t_end - t_start))

    return array[max_from:max_to+1]

def brute_forceV2(array):
    t_start = time.clock()
    max = 0
    size = len(array)
    max_from = max_to = 0
    for minIndex in range(0, size - 1):
        sum = array[minIndex]
        for index in range(minIndex+1, size):
            sum += array[index]

            if (sum > max):
                max = sum
                max_from = minIndex
                max_to = index
    t_end = time.clock()
    print ("Better BF finished in time: %8.8f" %(t_end - t_start))

    return array[max_from:max_to+1]

div_start = 0
div_end = 0
mid_start = 0
mid_end = 0
div_max = 0

def maxMiddle(array, start, middle, end):
	sum = 0
	left_sum = 0
        global mid_start
        global mid_end

	# left
	i = middle
	for index in range(i, start-1, -1):
		sum += array[index]
		if (sum > left_sum):
			left_sum = sum
                        mid_start = index

	# right
	sum = 0
	right_sum = 0
	i = middle + 1
	for index in range(i, end+1):
		sum += array[index]
		if(sum > right_sum):
			right_sum = sum
                        mid_end = index

	return left_sum + right_sum


def maxSub(array, start, end):
	# type: (object, object, object) -> object
	if(start == end):
		return array[start]

	middle = (start + end) / 2
	sub1 = maxSub(array, start, middle)
	sub2 = maxSub(array, middle+1, end)
        mid = maxMiddle(array, start, middle, end)
	result = max(max(sub1, sub2), mid)

#	print("max(",start,"-",end,") = ", result )

	global div_start
        global div_end
        global mid_start
        global mid_end
        global div_max
        
        if div_max < result:
            if sub1 == result:
                div_start = start
                div_end = middle
            elif sub2 == result:
                div_start = middle+1
                div_end = end
            else:
                div_start = mid_start
                div_end = mid_end
            div_max = result

	return result


def divConquer(array):
    global div_max
    div_max = 0
    t_start = time.clock()

    length = len(array) - 1   #accounts for zero-index
    result = maxSub(array, 0, length)

    t_end = time.clock()
    print ("Divide and Conquer finished in time: %8.8f" %(t_end - t_start))

    global div_start
    global div_end
#    print "max (" + str(div_start) + "-" + str(div_end) + ")"
    return array[div_start:div_end+1]

def generate_random_list(size):
    import random

    result = []
    array = []
    for n in range(size):
        array.append(random.randint(-99, 99))    

    result.append(array)

    return result

param = sys.argv
if len(param) < 3:
    print "Argument missing"
    print "python type maxsum.py input.txt output.txt"
    print "python type maxsum.py [size of random number list] output.txt rand"
    exit(-1)

numbers = []
if len(param) == 4:
    numbers = read_file(param[2])
if len(param) == 5:
    numbers = generate_random_list(int(param[2]))

print numbers
print "\n"

out = open(param[3], "wt")

for idx, arr in enumerate(numbers):
    sub_array = []
    if param[1] == "b":
        sub_array = brute_force(arr)
    elif param[1] == "b2":
        sub_array = brute_forceV2(arr)
    elif param[1] == "dc":
        sub_array = divConquer(arr)
    else:
        sub_array = max_subarray(arr)
    greatest_number = 0

    for n in sub_array:
        greatest_number += n
    if param[1] == "b":
        s = "[BF]The max of this array is:" + str(greatest_number)
    elif param[1] == "b2":
        s = "[BF2]The max of this array is:" + str(greatest_number)
    elif param[1] == "dc":
        s = "[DC]The max of this array is:" + str(greatest_number)
    else:
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
