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
