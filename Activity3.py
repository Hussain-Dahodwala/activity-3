'''
These functions are covering phase 1 and phase 2. Phase 1 sorts unsorted data provided in the parameter of the function using while loop.
Binary search function takes 2 parameters consisting array and target and returns output.
'''


import random
import time
def generate_sorted_data(size):
    '''this function takes data size as parameter and sorts the unsorted data using insertion sort'''
    data=[]
    for i in range(size): #uses size as range
        data.append(random.randint(1,100)) #takes random numbers as data
    print("unsorted data: ", data) #prints unsorted data
    for index in range(1, len(data)): #range is length of given data
        key  = data[index] 
        sub_index = index - 1 
        while  sub_index >= 0 and data[sub_index] > key: 
            data[sub_index + 1] = data[sub_index] 
            sub_index =  sub_index - 1 #subtracts by 1 to make condition false

        data[sub_index + 1] = key 
    return data



def binary_search(sorted_array, target):
     '''this function searches for the index of the given target value using binary search'''
     start = 0 #starting index
     end = len(sorted_array) - 1 #last index
     while start <= end:
        mid = (start+end)//2 #to not get float
        if sorted_array[mid]==target:
            return mid #if the middle most value = target, the index of middlemost value is returned
        elif sorted_array[mid]<target:
            start = mid + 1 #if target value is greater than middlemost value, the start value changes to mid + 1
        elif sorted_array[mid]>target:
            end = mid -1 # if target value is lesser than middlemost value, the end value changes to mid - 1
     if start>end:      
        return False #when start is greater than end, target value does not exist in array, so it returns false


'''This file contains code for phase 3 and 4'''
def merge_sort(data):
    '''This function uses merge sort algorithm to sort a unsorted list'''
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]#dividing in half
    right = data[mid:]
    left = merge_sort(left)# use of recursive function
    right = merge_sort(right)# use of recursive function, allowsfor splitting of the array to multiple single element arrays
    data_merged = []#empty list
    i = 0 # starting index for the left lists
    j = 0 # starting index for the right lists
    while i < len(left) and j < len(right):#comparing of first element of two arrays in order to merge
        if left[i] < right[j]:
            data_merged.append(left[i])#sorting of data using merging
            i += 1
        else:
            data_merged.append(right[j])#sorting of data using merging
            j += 1
    while i < len(left):#sorting of data using merging if condition for j is broken
        data_merged.append(left[i])#sorting of data using merging
        i += 1
    while j < len(right):#sorting of data using merging if condition for i is broken
        data_merged.append(right[j])
        j += 1
    return data_merged # returning of sorted array

def linear_search(data, target):
    '''this function uses linear search to find the target's index'''
    for i in range(len(data)):
        if data[i] == target:
            return i

def linear_search_time(sorted_data,target):
    '''function calculates time taken for linear search find the target '''
    start_time = time.perf_counter()#the time at which function start
    linear_index = linear_search(sorted_data, target)
    end_time = time.perf_counter()#the time at which function end
    linear_time = end_time - start_time#net time
    return linear_time
    

def binary_search_time(sorted_data,target):
    '''function calculates time taken for linear search find the target '''
    start_time = time.perf_counter() #the time at which function start
    binary_index = linear_search(sorted_data, target)
    end_time = time.perf_counter()#the time at which function end
    binary_time = end_time - start_time#net time
    return binary_time



