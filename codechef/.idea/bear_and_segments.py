def construct_tree(inpt, tree, low, high, pos, left):
    global p, maxp, count
    if low == high:
        tree[pos] = (inpt[low] % p)
        return
    mid = (low+high)//2
    construct_tree(inpt, tree, low, mid, 2*pos + 1, True)
    construct_tree(inpt, tree, mid+1, high, 2+pos + 2, False)
    if left:
        temp = max(tree[2*pos + 1]+tree[2*pos + 2] % p, tree[2*pos + 1]+tree[2*pos + 2]+tree[2*pos + 3] % p, tree[2*pos + 4]+tree[2*pos + 2]+tree[2*pos + 3] % p, tree[2*pos + 2]+tree[2*pos + 3] % p, tree[2*pos + 1], tree[2*pos + 2])
    else:
        temp = max(tree)
    if temp == maxp:
        



t = int(input())
while t:
     t -= 1
     n, p = map(int, input().split())
     a = list(map(int, input().split()))
     tr = [0]*100000
