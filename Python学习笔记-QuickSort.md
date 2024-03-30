
DATE: 2024_03_29

# 001-QuickSort 快速排序

#### 算法核心 

1. 将一个给定的值（一般取第一个或最后一个元素）作为基准，把比它大的元素放到一边，把比它大的元素放到另一边，
- Take a given value (usually the first or last element) as a pivot, put elements larger than it on one side, and put elements smaller than it on the other side.

2. 然后再次对两边分别作相同的操作。
- Then, repeat the same operation separately on both sides.

#### 代码
```
def partition(arr,l,h):
	
	i=l-1
	p=arr[h] #将最后一个元素设置为pivot
		
	for j in range(l,h): #在全队中寻找比pivot小的元素，确保他们置于队伍的前部的l到i位
		if arr[j]<=p:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	
	arr[i+1],arr[h]=arr[h],arr[i+1] #p在队中的位置，也就是第i+1位
	
	return i+1 #即分界线元素所在的位置	


def qsort(arr,left,right):
	if left<right:
		k=partition(arr,left,right) #通过调用partition来寻找分界线
		qsort(arr,left,k-1) #对左边进行排序
		qsort(arr,k+1,right)

a=[1,9,10,8,7,2,6,4,5]
qsort(a,0,len(a)-1)
print(a)

```

当然，在询问了chatGPT之后，因为python有很多很简洁的语法，所以还有一个更明快且符合直觉的版本：
```
def quicksort(arr):
	if len(arr)<=2:
		return arr
	else:
		p=arr[0]
		leftarr=[x for x in arr[1:] if x<=p]
		rightarr=[x for x in arr[1:] if x>=p]
		return quicksort(leftarr)+[p]+quicksort(rightarr)

a=[1,9,10,8,7,2,6,4,5]
print(quicksort(a))
		
```

由于这个版本直接把左右两边丢进新数组里，而不需要用通过交换反复操作同一个数组以及反复确认i和j指针所在的位置，更便于我这种菜鸟的理解一些。

#### 算法的复杂度：需要比较和交换多少次？

不过，快速排序到底有多快呢？算法书里往往直接给出O(n log(n))的平均时间复杂度以及最坏情况下退化到 n^2 的水平。那么这个平均值结论是如何得到的呢。这里，我们以平均的操作次数来估算这个算法的复杂度。

我们假设对一个N个元素的数组，
1. 在执行回溯之前的partition段落里，总共操作（判断比较/交换）了N+1次：
2. 然后我们考虑回溯部分调用：
		选择的分界线实际是第k位的概率是：1/n
		那么调用的子过程分别涉及到的就是k-1个元素的快排和n-k个元素的快排

得到了递推数列：

$$C_n=n+1+\sum_{k=1}^n \frac{1}{N} (C_{k-1}+C_{n-k})$$
我们注意到，求和内部的Ck-1和Cn-k事实上是对称的。（若展开其实只不过是同一序列的顺序和逆序排列）那么很容易得到他们的合相等，则得到下式：
$$C_n=N+1+\frac{2}{N} \sum_{k=1}^nC_{k-1}$$

要想求解Cn,两边同时乘以N，移项，后得到下式，记为A：
$$NC_n=N(N+1)+2\sum_{k=1}^nC_{k-1}$$
此时我们将此式带入n-1的再写一遍得到下式，记为B：
$$(N-1)C_{n-1}=N(N-1)+2\sum_{k=1}^{n-1}C_{k-1}$$
用A-B则消除求和式，得到：
$$NC_n-(N-1)C_{n-1}=2N+2C_{n-1}$$
整理后得到：
		$$NC_n=2N+(N+1)C_{n-1}$$
此时，两边同除以N（N+1），得：
		$$\frac{C_n}{N+1}=\frac{2}{N+1}+\frac{C_{n-1}}{N}$$
不难注意到此时展开：
	$$ \frac{C_n}{N+1}=C_0+1+\frac23+…\frac2N+\frac2{N+1}=2(H_{n+1}-1)$$

$$C_n=2(N+1)H_n-2N$$
由于*调和数：H_n～ln(n)+γ 
渐近分析 可知 Cn接近于 2N*ln(N)的复杂度（考虑N趋于无穷大时：）
	$$ \lim_{n\to\infty}\frac{Cn}{2NlnN}=\lim_{n\to\infty}\frac{2NlnN+2LnN-2N}{2NlnN}=1 $$

由此 我们就得到了快速排序的平均时间复杂度。

#### 展望：
当然，我们也可以编程验证此事：只需要取大量的n再进行大量的重复实验，实验结果点阵图应当和上述曲线接近。

#### References
https://www.coursera.org/learn/analysis-of-algorithms/
https://aofa.cs.princeton.edu/home/