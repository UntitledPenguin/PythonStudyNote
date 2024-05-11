import heapq 
import random
def bubbleup_max(heap, root):
    endpos = len(heap)
    startpos = root
    newitem = heap[pos]
    # Bubble up the larger child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of larger child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[rightpos] < heap[childpos]:
            childpos = rightpos
        # Move the larger child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem

#我们使用random生成10个随机元素，然后把它们扔进堆里
h = [random.randint(1, 100) for _ in range(10)] 
print("随机生成的数列：", h) 

heapq.heapify(h) 
print("转换为最小堆后的数列：", h) 
#直接调用最小值：
min = h[0]
print("最小元素：", min) 
print("剩余的堆元素：", h) 
#提取最小值
min = heapq.heappop(h) 
print("弹出的最小元素：", min) 
print("剩余的堆元素：", h) 

# 向堆中插入一个新的随机数字 
x = random.randint(1, 100) 
heapq.heappush(h, x) 
print("插入新元素后的堆：", h) 



heapq._heapify_max(h) 
print("转换为最大堆后的数列：", h) 
#直接调用最大值：
max = h[0]
print("最大元素：", max) 
print("剩余的堆元素：", h) 
#提取最大值
min = heapq._heappop_max(h) 
print("弹出的最大元素：", max) 
print("剩余的堆元素：", h) 

# 向堆中插入一个新的随机数字 
x = random.randint(1, 100) 
h.append(x)
print("插入后的堆：", h) 
heapq._siftdown_max(h, 0, len(h)-1)
print("插入新元素后的堆：", h) 