N = int(input())

arr = [list(input().split()) for _ in range(N)]


class Node():
    def __init__(self, item, l, r):
        self.item = item
        self.l = l
        self.r = r


node_map = dict()

for node in arr:
    item, l, r = node
    node_map[item] = Node(item, l, r)

preorder_result = ''
inorder_result = ''
postorder_result = ''


# 전위순회
def preorder(node: Node):
    global preorder_result

    preorder_result += node.item
    if node.l != '.':
        preorder(node_map.get(node.l))
    if node.r != '.':
        preorder(node_map.get(node.r))


# 중위순회
def inorder(node: Node):
    global inorder_result

    if node.l != '.':
        inorder(node_map.get(node.l))
    inorder_result += node.item
    if node.r != '.':
        inorder(node_map.get(node.r))


# 후위순회
def postorder(node: Node):
    global postorder_result

    if node.l != '.':
        postorder(node_map.get(node.l))
    if node.r != '.':
        postorder(node_map.get(node.r))
    postorder_result += node.item


preorder(node_map[arr[0][0]])
inorder(node_map[arr[0][0]])
postorder(node_map[arr[0][0]])

print(preorder_result)
print(inorder_result)
print(postorder_result)
