


# Python program for implementation of Quicksort Sort
# This implementation utilizes pivot as the first element in the nums list
# Sorting n interger in given scale
# Date:2024 March 27

import random
    
def QuickSort(lst):
    if len(lst)<2: return lst
    if len(lst)==2:
        if lst[0]>lst[1]:
            s=lst[0]
            lst[0]=lst[1]
            lst[1]=s 
        return lst
    else:
        p=lst[0] #extract pivotal value
        i=1
        l=len(lst)
        j=l-1
        while i<j:            
            while i<j and lst[i]<=p: i+=1
            while j>=i and lst[j]>=p: j-=1
            if i<j:
                s=lst[i]
                lst[i]=lst[j]
                lst[j]=s
        x=lst[j]
        lst[j]=p
        lst[0]=x
        if j>0: lst[:j]=QuickSort(lst[:j])
        if j<l-1:lst[j+1:]=QuickSort(lst[j+1:])
    return lst

n=int(input())
arr=[]
scale=int(input())
for k in range(n):
    arr.append(random.randint(0, scale))
print(arr)
print(QuickSort(arr))