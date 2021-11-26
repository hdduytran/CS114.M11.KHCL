from sys import stdin

def input():
    return stdin.readline()

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def Insert(self, data):
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.Insert(data)
    elif data > self.data:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.Insert(data)

def height(Node):
	if Node is None:
		return 0
	else:
		l = height(Node.left)
		r = height(Node.right)
	if l > r:
		return l + 1
	else:
		return r + 1

a = []
while 1:
  k = [int(i) for i in input().split()]
  if k[0] == 0:
    try:
      idx = a.index(k[1])
      a.pop(idx)
      a.insert(0,k[1])
    except:
      a.insert(0,k[1])
  elif k[0] == 1:
    if k[1] not in a:
      a.append(k[1])
  elif k[0] == 2:
    try:
      idx_a=a.index(k[1])
      if k[2] in a:
        idx_b = a.index(k[2])
        if idx_a < idx_b:
          a.pop(idx_b)
          a.insert(idx_a+1, k[2])
      else:
        a.insert(idx_a+1, k[2])
    except:
      a.insert(0, k[2])
  else:
    root = Node(a[0])
    break

for i in range(1, len(a)):
  root.Insert(a[i])

print(height(root))