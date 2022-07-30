import math
'''
The function sum_of_value adds up all the numbers of the entered array, which are completely divisible by the entered value,

For example – If the entered array is arr{1,2,3,4,5}, and the entered value is 2, then the output will be 2+4 = 6.
'''
def sum_of_value(len, arr, value):
    sum = 0
    for i in range(0, len):
        if math.fmod(arr[i], value) == 0:
            sum = + arr[i]
    print("sum is :",sum)
    return sum

number_array = [10,20,30]
sum_of_value(3,number_array,5)