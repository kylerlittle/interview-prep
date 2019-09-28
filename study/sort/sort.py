from typing import List
import numpy as np
from statistics import median

def median_of_three(nums: List[int], left: int, right: int) -> int:
    """Returns index of median of three
    """
    mid = int((left - right) / 2)
    midNum = nums[mid]
    leftNum = nums[left]
    rightNum = nums[right]

    if leftNum < midNum <= rightNum:
        return mid
    elif midNum < leftNum <= rightNum:
        return left
    else:
        return right

def swap(nums: List[int], i: int, j: int):
    """Swaps elements i and j in nums
    """
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def __quicksort__(nums: List[int], left: int, right: int) -> List[int]:
    """Recursively quicksort elements nums[left : right + 1]
    """
    # 0. base case
    if right <= left:
        return

    # 1. pick a pivot -- we'll use median of 3
    # choosing a bad pivot everytime gives us worst case
    pivot = median_of_three(nums, left, right)
    pivotVal = nums[pivot]

    # 2. put pivot at rightmost position
    swap(nums, pivot, right)

    # 3. move all elements < nums[pivot] to left
    #    all elements >= nums[pivot] to right
    # notes:
    # idea is have an ptr point to next avail slot for left/right
    # when you find an item < mid, put it at leftAvail; leftAvail++
    # same thing required for quickselect
    # except in quickselect you only recurse on one half or
    # simply find your kth smallest
    leftNextAvail = i = left

    # iterate until where we put the pivot
    while i < right:
        if nums[i] < pivotVal:
            # put element at leftNextAvail
            swap(nums, i, leftNextAvail)
            leftNextAvail += 1
        i += 1
    
    # 4. put pivot back in its correct position
    swap(nums, leftNextAvail, right)
    
    # 5. recurse on the left half, recurse on the right half
    __quicksort__(nums, left, leftNextAvail - 1)
    __quicksort__(nums, leftNextAvail + 1, right)

def quicksort(nums: List[int]) -> List[int]:
    """
    Quicksorts a list. The idea is fairly simple. Think *quickselect*.
    We randomly select an element that is hopefully the median of the
    array. Then move everything < to left, everything > to right, recurse.

    Pros:
    - practically extremely fast

    Cons:
    - worst case runtime is O(n^2)

    """
    # edge case
    if len(nums) <= 1:
        return nums

    __quicksort__(nums, 0, len(nums) - 1)

    return nums

def mergesort(nums: List[int]) -> List[int]:
    """
    Mergesorts a list. The overarching idea is simple: 'it's easy/fast
    to merge two sorted lists'

    Pros:
    - worst case runtime is O(n log n)

    Cons:
    -
    
    """
    pass

