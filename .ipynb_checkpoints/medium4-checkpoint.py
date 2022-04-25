def get_input():
    n = int(input())
    citations = [0] * n
    for i in range(n):
        citations[i] = int(input())
    return citations

def hIndex(citations):
        h = 0
        for i in range(len(citations)):
            count = 0
            for j in range(len(citations)):
                if citations[j] >= citations[i]:
                    count += 1
                if count >= citations[i] and citations[i] > h:
                    h = citations[i]
        return h
    
citations = get_input()
print(hIndex(citations))