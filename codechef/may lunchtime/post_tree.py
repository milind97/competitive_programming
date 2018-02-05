class node:

    def __init__(self, value):
        self.children = {}
        self.value = value

def main():
    n = int(input())
    parent = list(map(int, input().split()))
    val = list(map(int, input().split()))
    arr = [-1, node(val[0])]
    for i in range(1, n):
        arr.append(node(val[i]))
    print(arr)
    for i in range(n-1):
        arr[i+1]
if __name__ == "__main__":
    main()




