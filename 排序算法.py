#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:08:40 2018

@author: wangjian
"""
#1.插入排序：最坏O(n2)
#从第二个数字开始，分别和前边的比较，类似摆扑克牌一样
#当前面的数字大于后面的就开始插入，先把大的储存，然后插入到后边，再把小的给前边的
def insertSort(relist):
    len_ = len(relist)
    for i in range(1,len_):  
        for j in range(i):
            if relist[i] < relist[j]:
                relist.insert(j,relist[i]) 
                # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                relist.pop(i+1)
                # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出
                break
    return relist

print insertSort([1,5,3,4,6,7,0])
        

#2.归并排序：O(nlogn)
def merge(left,right):#合并函数
    #输入的left和right必须是排序好的
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #处理不等长或其他边界时：
    if i==len(left):#left已经没有了，所以直接全加上right
        for v in right[j:]:
            result.append(v)
    else:#left长，right已经没有了，所以全加上left
        for v in left[i:]:
            result.append(v)
    return result
    

#补：这是将两个有序数组合并成新的数组，若不生成新数组，把right直接合并到left中，则：
def merge2(left,right):
    l=len(left)
    r=len(right)
    while r>0:
        if l<=0 or left[l-1]<=right[r-1]:
            left[l+r-1]=right[r-1]
            r-=1
        else:
            left[l+r-1]=left[l-1]
            l-=1
#这种方法要掌握，比较大小后，以大的为标准
            
def merge_list(lists):#分割函数
    #递归实现，把一个list进行分割成两个已经排序好的子序列
    if len(lists)<=1:
        return lists
    length=len(lists)/2
    left=merge_list(lists[:length])
    right=merge_list(lists[length:])
    return merge(left,right)

print merge_list([1,5,3,4,6,7,0])



#3冒泡排序：O(n2)
def f(lists):
    length=len(lists)
    for i in range(length):
        for j in range(i+1,length):#反复交换相邻的未按次序排列的元素
            if lists[j]<lists[i]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists
print f([1,5,3,4,6,7,0])



#4 堆排序：O(nlogn)
#思路： 先把数组构造成完全二叉树，然后交换根节点和最后一个节点；固定最后一个，对前n-1个，重复
#排序使用最大堆，构造优先队列使用最小堆

①建堆，建堆是不断调整堆的过程，从len/2处开始调整，一直到第一个节点，此处len是堆中元素的个数。
建堆的过程是线性的过程，从len/2到0处一直调用调整堆的过程，相当于o(h1)+o(h2)…+o(hlen/2) 
其中h表示节点的深度，len/2表示节点的个数，这是一个求和的过程，结果是线性的O(n)。
②调整堆：调整堆在构建堆的过程中会用到，而且在堆排序过程中也会用到。
利用的思想是比较节点i和它的孩子节点left(i),right(i)，选出三者最大(或者最小)者，
如果最大（小）值不是节点i而是它的一个孩子节点，那边交互节点i和该节点，
然后再调用调整堆过程，这是一个递归的过程。
调整堆的过程时间复杂度与堆的深度有关系，是lgn的操作，因为是沿着深度方向进行调整的。
③堆排序：堆排序是利用上面的两个过程来进行的。
首先是根据元素构建堆。然后将堆的根节点取出(一般是与最后一个节点进行交换)，
将前面len-1个节点继续进行堆调整的过程，然后再将根节点取出，这样一直到所有节点都取出。
堆排序过程的时间复杂度是O(nlgn)。因为建堆的时间复杂度是O(n)（调用一次）；
调整堆的时间复杂度是lgn，调用了n-1次，所以堆排序的时间复杂度是O(nlgn)[2] 
#（1）调整堆
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    for i in range(0, (int(size/2)))[::-1]:
        adjust_heap(lists, i, size)

# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)#创建
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]#交换
        adjust_heap(lists, 0, i)#调整
    return lists

print heap_sort([1,5,3,4,6,7,0])

            


#5.快速排序 期望O(nlogn)，最坏O(n^2)
#分治思想
#通过一趟排序将要排序的数据分割成独立的两部分
#其中一部分的所有数据都比另外一部分的所有数据都要小
#然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行
#如序列[6，8，1，4，3，9]，选择6作为基准数。
#从右向左扫描，寻找比基准数小的数字为3，交换6和3的位置，[3，8，1，4，6，9]，
#接着从左向右扫描，寻找比基准数大的数字为8，交换6和8的位置，[3，6，1，4，8，9]。
#重复上述过程，直到基准数左边的数字都比其小，右边的数字都比其大。
#然后分别对基准数左边和右边的序列递归
#快速排序（Quicksort）是对冒泡排序的一种改进。
#改进：关于这一改进的最简单的描述大概是这样的：与一般的快速排序方法不同，它并不是选择待排数组的第一个数作为中轴，而是选用待排数组最左边、最右边和最中间的三个元素的中间值作为中轴。这一改进对于原来的快速排序算法来说，主要有两点优势：
#（1） 首先，它使得最坏情况发生的几率减小了。
#（2） 其次，未改进的快速排序算法为了防止比较时数组越界，在最后要设置一个哨点。
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList




#以上排序算法都是比较排序，最坏都得O(nlogn)
#下边介绍线性时间复杂度排序：计数排序，基数排序和通排序


#7.基数排序
#8.桶排序
#桶排序的原理很简单，就是设置一个个的桶，将需要排序的对象列表按顺序放入桶里面。 
#桶排序对于相同对象特别多的列表速度特别快。但是遗憾的是需要排序的对象必须是已知的数值。 
#桶排序可以应用在排列考试成绩等等的场景里面
#（因为数千人、数万人的成绩只有数百个，拥有同一成绩的人特别多）
def bucket(lst):
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        buckets[lst[i]-min(lst)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res
print bucket([1,5,3,4,6,7,0])


#9.选择排序，平均O(n^2)
#每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置
#直到全部待排序的数据元素排完
def selectionSort(alist):
    for i in range(len(alist)-1):
        min = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))


#10.希尔排序，时间复杂度为：O(nlogn)，该方法实质上是一种分组插入方法
#一般的初次取序列的一半为增量，以后每次减半，直到增量为1。
#希尔排序是唯一能在效率上与快速排序一较高低的算法
#先将序列分成较多个子序列分别进行排序，再分成较少个子序列分别进行排序，直到最后为一个序列排序。
#希尔排序与快速排序都基于“分治法”
#1.1如何划分子序列：希尔排序采用每隔固定距离选取一个数的方法划分子序，称为增量
#1.2子序内部怎么排序：希尔排序的子序排序方法为插入排序
其实就是比较相等间隔的数字，随着间隔逐渐减小到1，排序完成
L = [54,26,93,17,77,31,44,55,20]
def Shell_sort(L):
    step = len(L)/2
    while step > 0:
        for i in range(step,len(L)): 
        # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
        #在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while(i >= step and L[i] < L[i-step]):      
        #这里可以调整step从小到大或者从大到小排列
                L[i],L[i-step] = L[i-step],L[i]
                i -= step
        step /= 2
    return L
print Shell_sort(L)



时间复杂度：
O(n*n)
插入排序、选择排序和冒泡排序


O(nlogn)
快速排序、堆排序和归并排序

（1）若n较小（数据规模较小），插入排序或选择排序较好
（2）若数据初始状态基本有序（正序），插入、冒泡或快速排序为宜
（3）若n较大，则采用时间复杂度为O(nlogn)的排序方法：快速排序或堆排序
（4）快速排序是目前基于比较的排序中被认为是最好的方法，当待排序的关键字是随机分布时，快速排序的平均时间最短；
（5）堆排序所需的辅助空间少于快速排序，并且不会出现快速排序可能出现的最坏情况。这两种排序都是不稳定的。


快速排序的时间性能取决于快速排序的递归深度，可以用递归树来描述递归算法的执行情况 
在关键字已经基本有序的情况下（正序或者逆序），每次划分都只得到一个比上一次划分少一个记录的子序列，
此时需要执行n-1次递归调用，且第i次划分需要经过n-i次关键字的比较才能找到第i个记录，
比较次数达到(n(n-1))/2，最终其时间复杂度为O(n*n)




















