def solution(n, times):
    left =1
    right = n* max(times)
    answer = right+1
    while left <= right:
        mid = (left+right)//2
        result =0
        for time in times:
            result += (mid//time)
        print(left,right)
        
        
        if result < n :
            left = mid + 1
            
        else:
            answer = mid 
            right = mid - 1
            
    return answer