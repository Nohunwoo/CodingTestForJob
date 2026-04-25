def solution(nums):
    num_type = len(set(nums))
    num_half = len(nums)/2
    return min(num_type,num_half)