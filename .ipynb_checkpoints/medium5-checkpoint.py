def get_input():
    n = int(input())
    intervals = []* n
    for i in range(n):
        intervals.append([0,0])
        for j in range(2):
            intervals[i][j] = input()
    return intervals

def merge(intervals):
        i = 0
        while i < (len(intervals)-1):
            j = i+1
            while j <len(intervals):
            
                if (intervals[i][0] > intervals[j][0] and intervals[i][0] < intervals[j][1]) or (intervals[i][1] > intervals[j][0] and intervals[i][1] < intervals[j][1]):
                    intervals[i] = [min(intervals[i][0],intervals[i][1], intervals[j][0], intervals[j][1]), max(intervals[i][0],intervals[i][1], intervals[j][0], intervals[j][1])]
                    intervals.pop(j)
                j+=1
            i+=1
        return intervals

intervals = get_input()
print(merge(intervals))