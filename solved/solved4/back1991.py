import sys
input = sys.stdin.readline

change = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
    'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
    'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25, '.': -100,
}
change2 = {v:k for k,v in change.items()}

n = int(input())
tree = [[] for _ in range(n)]
for i in range(n):
    p, left, right = map(str, input().split())
    p = change[p]
    left = change[left]
    right = change[right]
    tree[p] = (left, right)

preorder = []
inorder = []
postorder = []
def dfs(node):
    preorder.append(change2[node])
    childs = tree[node]
    left, right = childs[0], childs[1]
    if left >= 0:
        dfs(left)
    inorder.append(change2[node])
    if right >= 0:
        dfs(right)
    postorder.append(change2[node])

dfs(0)
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))