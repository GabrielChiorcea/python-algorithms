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
