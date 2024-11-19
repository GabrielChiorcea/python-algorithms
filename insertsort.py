
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
