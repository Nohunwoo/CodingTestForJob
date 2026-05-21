def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    while left <= right:
        peo = 0
        mid = (left + right) // 2
        for time in times:
            peo += mid // time
        if peo >= n:
            answer = mid
            right = mid -1
        else:
            left = mid +1
    return answer