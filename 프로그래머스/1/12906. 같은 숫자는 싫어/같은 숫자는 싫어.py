def solution(arr):
    answer = []
    
    for x in range(len(arr)):
        if arr[x] not in answer : 
            answer.append(arr[x])
            continue
        elif arr[x] != answer[-1] : answer.append(arr[x])
    
    return answer