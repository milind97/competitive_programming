class Trienode:

    def __init__(self):
        self.children = {}
        self.endofword = False
root = Trienode()


def insert(s):
    global root
    current = root
    for i in s:
        node = current.children.get(i)
        if node == None:
            node = Trienode()
            current.children[i] = node
        current = node
    current.endofword = True


def search(s):
    global root
    current = root
    ans = ''
    for i in s:
        ans += i
        node = current.children.get(i)
        if not node:
            return ans
        current = node
    else:
        return None

def main():
    n = int(input())
    bsites = []
    for i in range(n):
        s = input().strip()
        if s[0] == '-':
            bsites.append(s[2:])
        else:
            insert(s[2:])
    y = set()
    for site in bsites:
        temp = search(site)
        if temp:
            y.add(temp)
        else:
            print(-1)
            break
    else:
        print(len(y))
        [print(x) for x in sorted(y)]


if __name__ == '__main__':
    main()
