import numpy
import random
import time
def timeqs(elements):
    array=random.sample(range(1, elements+100), elements)
    curr = time.time()
    quicksort1(array)
    print(time.time()-curr)
    curr = time.time()
    quicksort2(array)
    print(time.time()-curr)
    curr = time.time()
    quicksort3(array)
    print(time.time()-curr)

def quicksort1(array):                       #random pivot
    smallerarray = list()
    largerarray = list()
    resultarray = list()
    if len(array)>2:
        pivot = random.randint(0,len(array)-1)#generate pivot
        for i in array :                      #split array according to pivot
            if i>array[pivot]:
                largerarray.append(i)
            else:
                smallerarray.append(i)
    elif len(array) == 2 :                    #base case array size is 2
        if array[0]>array[1]:
            largerarray.append(array[0])
            smallerarray.append(array[1])
        else:
            smallerarray.append(array[0])
            largerarray.append(array[1])
    elif len(array)==1:                       #base case size is 1
        
        resultarray.append(array[0])
        return resultarray
    else:
        return resultarray                   #base case len 0
    resultarray.extend(quicksort1(smallerarray))    #recursive calls on the two new half-arrays
    resultarray.extend(quicksort1(largerarray))
    return resultarray

def quicksort2(array):                       #median pivot
    smallerarray = list()
    largerarray = list()
    resultarray = list()
    if len(array)>2:
        if array[0]>array[len(array)//2] and array[0]<array[len(array)-1]:                #generate pivot
            pivot = 0
        elif array[0]<array[len(array)//2] and array[0]>array[len(array)-1]:
            pivot = 0
        elif array[1]>array[len(array)-1] and array[len(array)//2]<array[0]:
            pivot = len(array)//2
        elif array[1]<array[len(array)-1] and array[len(array)//2]>array[0]:
            pivot = len(array)//2
        elif array[len(array)-1]>array[len(array)//2] and array[len(array)-1]<array[0]:
            pivot = len(array)-1
        elif array[len(array)-1]<array[len(array)//2] and array[len(array)-1]>array[0]:
            pivot = len(array)-1
        for i in array :                     #split array according to pivot
            if i>array[pivot]:
                largerarray.append(i)
            else:
                smallerarray.append(i)
    elif len(array) == 2 :                   #base case array size is 2
        if array[0]>array[1]:
            largerarray.append(array[0])
            smallerarray.append(array[1])
        else:
            smallerarray.append(array[0])
            largerarray.append(array[1])
    elif len(array)==1:                      #base case size is 1
        
        resultarray.append(array[0])
        return resultarray
    else:
        return resultarray                   #base case len 0
    resultarray.extend(quicksort1(smallerarray))    #recursive calls on the two new half-arrays
    resultarray.extend(quicksort1(largerarray))
    
    return resultarray

def quicksort3(array):
    smallerarray = list()
    largerarray = list()
    resultarray = list()
    if len(array)>2:
        pivot = genpivot(array)#generate pivot
        for i in array :                      #split array according to pivot
            if i>array[pivot]:
                largerarray.append(i)
            else:
                smallerarray.append(i)
    elif len(array) == 2 :                    #base case array size is 2
        if array[0]>array[1]:
            largerarray.append(array[0])
            smallerarray.append(array[1])
        else:
            smallerarray.append(array[0])
            largerarray.append(array[1])
    elif len(array)==1:                       #base case size is 1
        
        resultarray.append(array[0])
        return resultarray
    else:
        return resultarray                   #base case len 0
    resultarray.extend(quicksort1(smallerarray))    #recursive calls on the two new half-arrays
    resultarray.extend(quicksort1(largerarray))
    
    return resultarray

def genpivot(array):
    count = list()
    largest = 0
    for i in array :
        if i > largest:
            largest = i
    i = 0
    while i <= largest:
        count.append(0)
        i = i+1
    for i in array:
        count[i]=count[i]+1
    largest = 0             #how many times it recurs
    largestindex = 0        #most recurring value
    index = 0               #current index
    for i in count:
        if i > largest:
            largest = i
            largestindex = index
        index=index+1
    index = 0
    for i in array:
        if i == largestindex:
            break
        else:
            index=index+1
    return index
    #gör listan lika lång som array, sätt alla värden till 0 addera +1 vid index = värdet som dyker upp i array
