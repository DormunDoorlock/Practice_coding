def fibonacci(k):
    f = [0,1,1]
    for n in range(3,k+1):
        f.append((f[n-1]+f[n-2])%1234567)
        
    return f[k]

def solution(n):
    answer = fibonacci(n) 
    return answer