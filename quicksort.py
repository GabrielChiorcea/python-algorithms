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



