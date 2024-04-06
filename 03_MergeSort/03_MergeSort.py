import math

def mergesort(arr):
    if len(arr)<2:
         return arr
    mid=len(arr)//2 
    lft=arr[:mid]
    rgt=arr[mid:]
    
    lft=mergesort(lft)
    rgt=mergesort(rgt)

    return merge(lft,rgt)

def merge(a_l,a_r):
     merged=[]
     i=0
     j=0
     while (i<len(a_l)) and (j<len(a_r)):
          if a_l[i]<a_r[j]:
               merged.append(a_l[i])
               i+=1
          else:
               merged.append(a_r[j])
               j+=1
     while i<len(a_l): 
        merged.append(a_l[i]) 
        i+=1
     while j<len(a_r): 
        merged.append(a_r[j]) 
        j+=1   
     return merged

import random

n=int(input())
arr=[]
scale=int(input())
for k in range(n):
    arr.append(random.randint(0, scale))
print(arr)
print(mergesort(arr))


