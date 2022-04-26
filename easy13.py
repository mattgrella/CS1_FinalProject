def get_input():
    n = int(input())
    edges = []* n
    for i in range(n):
        edges.append([0,0])
        for j in range(2):
            edges[i][j] = input()
    return edges

def findCenter(edges):
    if edges[0][0] in edges[1]:
        return edges[0][0]
    else:
        return edges[0][1]

edges = get_input()
print(findCenter(edges))