array = [1, 3, 7, 9, 15, 18, 21, 25]
x = 15

def bsy(array, n):
    start_index = 0
    midel_index = 0
    loop_time = 0
    last_index = len(array) - 1
    print(f"The maximum index is {last_index}")
    
    while start_index <= last_index:
        midel_index = (start_index + last_index) // 2
        keep_last_index = last_index
        print(f"The middle index is {midel_index}")
        
        loop_time += 1
        if array[midel_index] == n:
            print(f"Found the number on attempt {loop_time}, it is at index {midel_index}")
        
        if array[midel_index] < n:
            start_index = midel_index + 1
            print(f"Start was 0, now it is {start_index}")
        else:
            last_index = midel_index - 1
            print(f"The last index was {keep_last_index}, now it is {last_index}")
    
    return -1

bsy(array, x)

def insert_sort(array):
     for i in range(1, len(array)):
         left_val = i -1
         right_val = array[i]

         while left_val >= 0 and array[left_val] > right_val:
             array[left_val + 1] = array[left_val]
             left_val -= 1
     array[left_val + 1] = right_val

 print(array)
 insert_sort(array);
 print(array)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
