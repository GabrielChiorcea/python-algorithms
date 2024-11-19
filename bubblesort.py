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
