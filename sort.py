array = [1, 3, 7, 9, 15, 18, 21, 25]
x = 15

#Binary sort, cunoscut și sub numele de sortare binară prin inserție, este o variație a algoritmului de insert sort care utilizează 
#căutarea binară pentru a găsi poziția corectă de inserare a fiecărui element. În loc să parcurgă secțiunea sortată element cu element,
#binary sort folosește căutarea binară pentru a localiza rapid poziția potrivită, reducând astfel numărul de comparații necesare. După ce
#poziția corectă este determinată, elementul este inserat și restul listei este mutat pentru a face loc. Deși încă are o complexitate de timp de 
#O(n2) în cel mai rău caz, căutarea binară optimizează numărul de comparații, făcând algoritmul mai eficient decât insert sort pentru liste mari.

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



#Insert sort funcționează prin parcurgerea unei liste și inserarea fiecărui element în poziția corectă din secțiunea deja sortată a listei.
#Algoritmul începe cu al doilea element al listei și îl compară cu elementele precedente, mutându-l spre stânga până când găsește locul potrivit.
#Procesul se repetă pentru fiecare element din lista nesortată, până când întreaga listă devine sortată. Deși este simplu de înțeles și implementat, 
#insert sort este eficient doar pentru liste mici sau aproape sortate, având o complexitate de timp de O(n2) în cel mai rău caz.

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



#Bubble sort este un algoritm de sortare simplu, dar ineficient pentru liste mari. Funcționează prin parcurgerea 
#repetată a listei și compararea fiecărui pereche de elemente adiacente. Dacă două elemente sunt în ordine 
#greșită (de exemplu, primul este mai mare decât al doilea), acestea sunt interschimbate. Acest proces continuă 
#până când lista este parcurgă fără a se face nicio schimbare, semn că lista este sortată. Denumirea „bubble” provine din 
#faptul că valorile mari „bulează” spre sfârșitul listei după fiecare iterație. Algoritmul are o complexitate de timp de 
#O(n2) în cel mai rău și în cel mai bun caz, fiind astfel ineficient pentru liste mari.

def bubble_sort(array):
    for n in range(len(array) - 1, 0, -1):

        for i in range(n):
            if arr[i] > arr[i + 1]:
                
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

print("Unsorted list is:")
print(array)

bubble_sort(array)

print("Sorted list is:")
print(array)


#Heap sort transformă mai întâi array-ul într-un Max-Heap, asigurând că fiecare nod 
#părinte este mai mare decât copiii săi printr-un proces numit heapificare. Apoi, 
#elementul maxim (rădăcina heap-ului) este plasat la finalul array-ului, reducând 
#dimensiunea heap-ului și rearanjând restul elementelor pentru a restaura proprietatea 
#de Max-Heap. Acest proces de extragere a maximului și rearanjare se repetă până când toate elementele sunt sortate.

from heapq import heappush, heappop

def heapsort(list):
    heap = []
    for el in list:
        heappush(heap, el)
    sort = []

    while heap:
        sort.append(heappop(heap))
    
    return sort

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = heapsort(arr)
print(sorted_arr)



#legând un element numit pivot pentru a partiționa lista în două subliste: una cu elemente mai mici 
#sau egale cu pivotul și alta cu elemente mai mari. După partiționare, Quick Sort se aplică recursiv 
#pe fiecare sublistă până când listele devin suficient de mici (un singur element sau goale), moment
#în care sunt considerate sortate. La final, sublistele sortate sunt combinate împreună cu pivotul pentru
#a obține lista complet sortată. Alegerea pivotului influențează eficiența algoritmului, care în caz 
#optim și mediu are o complexitate de O(nlogn), dar poate ajunge la O(n2) în cazul cel mai defavorabil (partiționări dezechilibrate).



def quick_sort(arr):
    if len(arr) <= 1:  # Cazul de bază: lista este deja sortată dacă are 0 sau 1 element
        return arr
    pivot = arr[len(arr) // 2]  # Alegem pivotul ca elementul median
    left = [x for x in arr if x < pivot]  # Elemente mai mici decât pivotul
    middle = [x for x in arr if x == pivot]  # Elemente egale cu pivotul
    right = [x for x in arr if x > pivot]  # Elemente mai mari decât pivotul
    return quick_sort(left) + middle + quick_sort(right)  # Recurență și combinare

# Exemplu de utilizare
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Rezultatul va fi [1, 1, 2, 3, 6, 8, 10]
