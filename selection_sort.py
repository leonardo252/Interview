vet = [14,2,4,3,1,15,5,8,7,6,12,11,9,10,13]


def selection_sort(v):
    for posi in range(len(v)-1,0,-1):
        posi_max = 0
        for posi1 in range(1, posi+1):
            if v[posi1] > v[posi_max]:
                posi_max = posi1

        aux = v[posi]
        v[posi] = v[posi_max]
        v[posi_max] = aux

    return v

print(selection_sort(vet))
