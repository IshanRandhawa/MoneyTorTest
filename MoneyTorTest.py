

#question 1
#given constraints of 1,10 not taking care of case where 0 is present
#base answer
def power(a,b):
    return a**b
#implemented recursively
def power2(a,b):
    if b == 1:
        return a
    return a*(power(a,b-1))

#question2
#given time complexity is O(nlogn) the obvious case is to sort it and then add the unique elements to the front of the array and increase pointer
def removeduplicate(arr):
    arr.sort()
    index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1    
    return arr[:index]
    
# question3 base answers shouldn't use because of large constraints
def printfib1(n):
    arr = [0]*n
    arr[0],arr[1] = 0,1
    for i in range(2,n):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr)
#if we don't want to save the previous results we can just use 2 variables to keep count of the last 2 numbers because contraints are too large to keep a list in memory
def printfib2(n):
    f1,f2 = 0,1
    if n >= 0:
        print(0)
    if n >= 1:
        print(1)
    for i in range(2,n):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        print(f3)    


