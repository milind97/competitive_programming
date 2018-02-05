def step_count(a, b, steps):
    x = (b-a)/(steps-1)
    ans = [a]
    for i in range(steps-1):
        a += x
        ans.append(a)
    return ans

