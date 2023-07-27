



# 1:Implement Binary Search

def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# 2:Implement Merge Sort

def marge(x,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L = []
    R = []
    print(n1)

    for i in range(0,n1):
        L.append(x[l+i])

    for j in range(0,n2):
        R.append(x[m+1+j])

    i = 0 
    j = 0 
    k = 0

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            x[k] = L[i]
            i += 1
        else :
            x[k] = R[j]
            j += 1
        k+=1
    
    while i<n1:
        x[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        x[k] = R[j]
        j+=1
        k+=1

def margesort(x,l,r):
    if l<r:
        m= l+(r-l)//2
        margesort(x,l,m)
        margesort(x,m+1,r)
        marge(x,l,m,r)

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
margesort(arr,0,len(arr)-1)
print(arr)

# 3:Implement Quick Sort
def quicksort(x):
    if len(x) <= 1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return quicksort(l) + [p] + quicksort(r)
    
arr = [4,3,2,1,2,5,6,74,4]
sorted_array = quicksort(arr)
print(sorted_array)

# 4:Implement Insertion Sort
def insertionsort(x):
    l = len(x)
    if l<=1:
        return
    for i in range(1,l):
        n = x[i]
        j = i-1
        while j>=0 and n < x[j]:
            x[j+1] = x[j]
            j=j-1
        x[j+1]=n

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
insertionsort(arr)
print('insertion sort : ',arr)



# 5:Write a program to sort list of strings similar to that of dictionary    

lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
lst.sort() 
print(lst)




