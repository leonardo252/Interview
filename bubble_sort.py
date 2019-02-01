vet = [2,4,3,1,5,8,7,6,11,9,10]
#vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def bubble_sort(v):
    l = len(v)
    for i in range(0, l-1):
        for j in range(0, l-i-1):
            if(v[j] > v[j+1]):
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
                
    return v


def bubble_sort_flag(v):
    l = len(v)
    swap = False
    for i in range(0, l-1):
        for j in range(0, l-i-1):
            if(v[j] > v[j+1]):
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
                swap = True
        if (swap == True):
            swap = False
        else:
            return v

print(vet)        
print(bubble_sort(vet))
print(bubble_sort_flag(vet))

