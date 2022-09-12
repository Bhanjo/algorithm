import sys
sys.setrecursionlimit(10**8)

def preorder(sortY, sortX, temp):
    # 부모 노드 찾고, 부모의 x값 기준 index 찾기
    node = sortY[0]
    nodeIdx = sortX.index(node)
    
    leftNode = []
    rightNode = []
    
    for i in range(1, len(sortY)):
        # (부모노드 x값 > 자식의 x값) => 부모의 왼쪽에 붙을 노드
        if node[0] > sortY[i][0]:
            leftNode.append(sortY[i])
        else: # 부모의 오른쪽에 붙을 노드
            rightNode.append(sortY[i])
    
    # 전위순회
    temp.append(node[2])
    if leftNode: # 부모 노드 x값 기준 왼쪽 탐색
        preorder(leftNode, sortX[:nodeIdx], temp)
    if rightNode: # 부모 노드 x 값 기준 오른쪽 탐색
        preorder(rightNode, sortX[nodeIdx+1:], temp)
        
def postorder(sortY, sortX, temp):
    node = sortY[0]
    nodeIdx = sortX.index(node)
    
    leftNode = []
    rightNode = []
    
    for i in range(1, len(sortY)):
        if node[0] > sortY[i][0]:
            leftNode.append(sortY[i])
        else:
            rightNode.append(sortY[i])
    
    if leftNode:
        postorder(leftNode, sortX[:nodeIdx], temp)
    if rightNode:
        postorder(rightNode, sortX[nodeIdx+1:], temp)
    temp.append(node[2])
    

def solution(nodeinfo):
    pre, post = [], []
    
    # 각 노드 정보 => [x, y, 원래 번호]
    for idx, node in enumerate(nodeinfo):
        node.append(idx+1)
    
    # 순회에 쓸 매개변수
    sortY = sorted(nodeinfo, key=lambda x:(-x[1],x[0])) # y값 내림차순, x값 오름차순 정렬
    sortX = sorted(nodeinfo) # x값 오름차순으로 정렬
    
    preorder(sortY, sortX, pre)
    postorder(sortY, sortX, post)
    
    answer = [pre, post]
    return answer

# 2회차
import sys
sys.setrecursionlimit(10**6)

preorder = []
postorder = []

def pre(nodeinfo):
    if not nodeinfo: return
    top = nodeinfo[0]
    left, right = [], []

    for node in nodeinfo:
        if top[0] > node[0]: left.append(node)
        if top[0] < node[0]: right.append(node)

    preorder.append(top[2])
    pre(left)
    pre(right)

def post(nodeinfo):
    if not nodeinfo: return
    top = nodeinfo[0]
    left, right = [], []

    for node in nodeinfo:
        if top[0] > node[0]: left.append(node)
        if top[0] < node[0]: right.append(node)

    post(left)
    post(right)
    postorder.append(top[2])
        
def solution(nodeinfo):
    answer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))
    
    pre(nodeinfo)
    answer.append(preorder)
    post(nodeinfo)
    answer.append(postorder)
    
    return answer