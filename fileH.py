'''
These functions are covering phase 1 and phase 2. Phase 1 sorts unsorted data provided in the parameter of the function using while loop.
Binary search function takes 2 parameters consisting array and target and returns output.
'''


import random
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
var = (generate_sorted_data(10))

print(var)

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

print(binary_search(var, 72))
     

