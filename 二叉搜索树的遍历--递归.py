#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:31:12 2018

@author: wangjian
"""

class Node():
    def __init__(self,root):
        self.root=root
        self.lchild=None
        self.rchild=None

class Bitree():
    def __init__(self):
        self.root=None

    def insert(self,root,node):         #插入节点
        if root:
            if root.root>node.root:
                if root.lchild:
                    self.insert(root.lchild,node)
                else:
                    root.lchild=node
            else:
                 if root.rchild:
                     self.insert(root.rchild,node)
                 else:
                     root.rchild=node
        else:
          return 0

    def initBitree(self,data):        #生成二叉树
        root=Node(data[0])
        length=len(data)
        for x in range(1,length):
            node=Node(data[x])
            self.insert(root,node)
        return root


    def preoder(self,root):       #先序遍历
      if root:
        print(root.root)
        self.preoder(root.lchild)
        self.preoder(root.rchild)

    def midoder(self,root):      #中序遍历
        if root:
            self.midoder(root.lchild)
            print(root.root)
            self.midoder(root.rchild)

    def postoder(self,root):      #后序遍历
        if root:
            self.postoder(root.lchild)
            self.postoder(root.rchild)
            print(root.root)




if __name__ == '__main__':
    data=[3,7,5,8,9,10,11,2,6,4]
    Bitree=Bitree()
    a=Bitree.initBitree(data)
    print('前序遍历:')
    Bitree.preoder(a)
    print('中序遍历:')
    Bitree.midoder(a)
    print('后序遍历:')
    Bitree.postoder(a)