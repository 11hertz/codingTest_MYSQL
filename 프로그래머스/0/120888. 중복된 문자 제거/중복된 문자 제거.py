def solution(my_string):
    arr = []
    
    for x in my_string:
        if x not in arr: arr.append(x)
        else: continue

    return ''.join(arr)