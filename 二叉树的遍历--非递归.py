#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:26:24 2018

@author: wangjian
"""

class Node():
    #节点类
    def __init__(self,data = -1):
        self.data = data
        self.left = None
        self.right = None
class Tree():
    #树类
    def __init__(self):
        self.root = Node()

    def add(self,data):
        # 为树加入节点
        node  = Node(data)
        if self.root.data == -1:        #如果树为空，就对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:              #对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def pre_order_recursion(self,root):     #递归实现前序遍历
        if not root:
            return
        print root.data,
        self.pre_order_recursion(root.left)
        self.pre_order_recursion(root.right)

    def pre_order_stack(self,root):         #堆栈实现前序遍历（非递归）
        if not root:
            return
        myStack = []
        node = root
        while myStack or node:
            while node:       #从根节点开始，一直寻找他的左子树
                print node.data,
                myStack.append(node)
                node = node.left
            node = myStack.pop()    #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right       #开始查看它的右子树

    def in_order_recursion(self,root):      #递归实现中序遍历
        if not root:
            return
        self.in_order_recursion(root.left)
        print root.data,
        self.in_order_recursion(root.right)

    def in_order_stack(self,root):        #堆栈实现中序遍历（非递归）
        if not root:
            return
        myStack = []
        node = root
        while myStack or node:     #从根节点开始，一直寻找它的左子树
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print node.data,
            node = node.right


    def post_order_recursion(self,root):     #递归实现后序遍历
        if not root:
            return
        self.post_order_recursion(root.left)
        self.post_order_recursion(root.right)
        print root.data,
        
    def post_order_stack(self, root):  # 堆栈实现后序遍历（非递归）
        # 先遍历根节点，再遍历右子树，最后是左子树
        # 这样就可以转化为和先序遍历一个类型了，最后只把遍历结果逆序输出就OK了。
        if not root:
            return
        myStack1 = []
        myStack2 = []
        node = root
        while myStack1 or node:
            while node:
                myStack2.append(node.data)
                myStack1.append(node)
                node = node.right
            node = myStack1.pop()
            node = node.left
        print myStack2[::-1]

    def level_order_queue(self,root):       #队列实现层次遍历（非递归）
        if not root :
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.data,
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
                
if __name__ == '__main__':
    #主函数
    datas = [2,3,4,5,6,7,8,9]
    tree = Tree()          #新建一个树对象
    for data in datas:
        tree.add(data)      #逐个加入树的节点

    print '递归实现前序遍历：'
    tree.pre_order_recursion(tree.root)

    print '\n堆栈实现前序遍历'
    tree.pre_order_stack(tree.root)

    print "\n\n递归实现中序遍历："
    tree.in_order_recursion(tree.root)

    print "\n堆栈实现中序遍历："
    tree.in_order_stack(tree.root)

    print '\n\n递归实现后序遍历：'
    tree.post_order_recursion(tree.root)

    print '\n堆栈实现后序遍历：'
    tree.post_order_stack(tree.root)

    print '\n\n队列实现层次遍历：'
    tree.level_order_queue(tree.root)

    