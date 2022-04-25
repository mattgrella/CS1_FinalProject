def get_input():
    return input()
def longestValidParentheses(s):
    count = 0
    longest = 0
    i = 1
    while i < len(s):
        if s[i] == ')' and s[i-1] == '(':
            count += 2
            i+=2
            if count > longest:
                longest = count
        else:
            count = 0
            i += 1
    return longest
    
s = get_input()
print(longestValidParentheses(s))