import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, l, r = map(str, input().split())
    tree[root] = (l, r)


def preorder(root):
    print(root, end = '')
    left, right = tree[root]
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)
        
def inorder(root):
    left, right = tree[root]
    if left != '.':
        inorder(left)
    print(root, end='')
    if right != '.':
        inorder(right)

def postorder(root):
    left, right = tree[root]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(root, end='')
        

preorder('A')
print("")
inorder('A')    
print("")
postorder('A')