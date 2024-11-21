d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

#hard sort
# Sortare manuală (Insertion Sort)
def sort(arr):
    for i in range(1, len(arr)):
        cur_val = arr[i]
        pos = i - 1

        # Mutăm elementele mai mari la dreapta
        while pos >= 0 and arr[pos] > cur_val:
            arr[pos + 1] = arr[pos]
            pos -= 1

        # Inserăm valoarea curentă la locul ei
        arr[pos + 1] = cur_val

    return arr

# Crearea unui dicționar sortat pe baza valorilor sortate
def en(ds, nr):
    dc = {}
    used = set()  # Pentru a ține evidența cheilor deja adăugate

    for j in nr:  # Parcurgem valorile sortate
        for k, v in ds.items():
            if v == j and k not in used:  # Asociem valoarea cu cheia corespunzătoare
                dc[k] = v
                used.add(k)  # Marcăm cheia ca folosită
                break  # Ieșim din bucla internă pentru a evita duplicarea

    return dc

# Obținem valorile și le sortăm
myKeys = list(d.values())
keySort = sort(myKeys)

# Construim dicționarul sortat
new = en(d, keySort)

# Afișăm rezultatele
print("Valorile sortate:", keySort)
print("Dicționarul sortat:", new)


#soft sort
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# Sortăm valorile dicționarului
def sort_dict_by_values(ds):
    # Sortăm după valori și reconstruim dicționarul
    sorted_items = sorted(ds.items(), key=lambda item: item[1])
    return dict(sorted_items)

# Apelăm funcția
sorted_dict = sort_dict_by_values(d)

print(sorted_dict)

