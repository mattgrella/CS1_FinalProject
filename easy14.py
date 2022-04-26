def get_input():
    rings = input()
    return rings

def countPoints(rings):
    rods = {}
    for i in range(10):
        rods[i] = set()
    N = len(rings) // 2
    for i in range(N):
        color = rings[2*i]
        rod = int(rings[2*i + 1])
        rods[rod].add(color)
    count = 0
    for i in range(10):
        if len(rods[i]) == 3:
            count += 1
    return count

rings = get_input()
print(countPoints(rings))

