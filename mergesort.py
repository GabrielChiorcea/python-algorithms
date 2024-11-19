
#Merge sort este un algoritm de sortare eficient care folosește principiul „divide et impera”. Funcționează prin împărțirea recursivă a 
#listei în subliste mai mici până când fiecare sublistă conține un singur element sau este goală (fiind astfel sortată). Apoi, sublistele 
#sunt combinate printr-un proces de interclasare, în care elementele sunt comparate și adăugate într-o ordine sortată pentru a forma subliste 
#din ce în ce mai mari până când întreaga listă este reconstruită și sortată. Merge sort are o complexitate de timp de 
#O(n log n) în toate cazurile, ceea ce îl face mult mai eficient decât sortările simple precum insert sort, mai ales pentru liste mari.

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
