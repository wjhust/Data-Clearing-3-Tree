#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:21:50 2018

@author: wangjian
"""
def Max(arr,low,high):#分治策略
    if low==high:
        return arr[low]
    mid=(low+high)//2
    m1=Max(arr,low,mid)#左边递归
    m2=Max(arr,mid+1,high)#右边递归
    
    tmp1=arr[mid]#跨越中间时，分别找到左，右两边的最大，加起来
    left=arr[mid]
    for i in range(mid-1,low-1,-1):
        tmp1+=arr[i]
        if tmp1>left:
            left=tmp1#让left每步都取当前最大
    tmp2=arr[mid+1]
    right=arr[mid+1]
    for i in range(mid+2,high+1):
        tmp2+=arr[i]
        if right<tmp2:
            right=tmp2
    m3=left+right  
    return max(m1,m2,m3)
   

arr=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5]
print Max(arr,0,len(arr)-1)



def max_child(arr):#动态规划处理，
	result = arr[0]
	sum1 = arr[0]
	for i in range(1, len(arr)):
	    if sum1 > 0:#sum1大于0才继续加，否则抛弃；
			sum1+= arr[i]
	    else:
			sum1 = arr[i]
	    if sum1 > result:
			result = sum1
	return result
 
print max_child(arr)