v = [ 9,1,5,7,2,4,8,6,3,0]


def merge (left, right):
    for i in range(right):
        left.append(right[i])
        print(left)   

    
def mergeSort(v):
    if (len(v) > 1):
        m = (len(v)) // 2
        L = v[:m]
        R = v[m:]
        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                v[k] = L[i] 
                i+=1
            else: 
                v[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            v[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            v[k] = R[j] 
            j+=1
            k+=1
        

mergeSort(v)
print(v)
