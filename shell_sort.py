v = [ 9,1,5,7,2,4,8,6,3,0]

n = len(v)

h = 1
while( h < n):
    h = 3*h+1

while(h > 0):
    h = h// 3
    for i in range(h, n):
        aux = v[i]
        j = i
        while( v[j-h] > aux and j>=h):
            v[j] = v[j-h]
            j = j - h
        v[j] = aux
    
    
print(v)

