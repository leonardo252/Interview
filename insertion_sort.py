vet = [14,2,4,3,1,15,5,8,7,6,12,11,9,10,13]

def insertion_sort(v):
    l = len(v)
    stR = 1
    endL = 0
    while(stR < l):
        pivo = stR
        for i in range(stR):
            if(v[i] > v[pivo]):
                aux = v[i]
                v[i] = v[pivo]
                v[pivo] = aux

        stR = stR + 1
        endL = endL + 1

    return(v)

  


insertion_sort(vet)

