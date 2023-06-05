# This problem was asked by Uber. Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers in the original array except the one at i.
# #### For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import unittest as ut


def day_two(input: list):
    prod = 1
    output = []
    for index in range(0, len(input)):
        prod *= input[index]

    for index in range(0, len(input)):
       output.append(int(prod / input[index]))

    return output

assert day_two([3,2,1]) == [2,3,6], f"Expected [2,3,6] got {day_two([3,2,1])}"
print("First case Passed!")

assert day_two([1,2,3,4,5]) == [120,60,40,30,24], f"Expected [120,60,40,30,24] got {day_two([1,2,3,4,5])}"
print("Second case passed!")