# https://www.acmicpc.net/problem/1991
# 트리 순회
# 

import sys
from collections import deque

input = sys.stdin.readline
NULL_VALUE = "."

n = int(input().strip())
nodes = {}
for _ in range(n):
    n1,n2,n3 = input().strip().split()
    nodes[n1] = [n2, n3]

# Step 1. 전위 순회
def preorder(node):
    if node == NULL_VALUE:
        return
    print(node, end="")
    preorder(nodes[node][0])
    preorder(nodes[node][1])

# Step 2. 중위 순회
def inorder(node):
    if node == NULL_VALUE:
        return
    inorder(nodes[node][0])
    print(node, end="")
    inorder(nodes[node][1])

# Step 3. 후위 순회
def postorder(node):
    if node == NULL_VALUE:
        return
    postorder(nodes[node][0])
    postorder(nodes[node][1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')