def solution(numbers, k):
    answer = 0
    times = len(numbers)
    answer = (2 * (k-1)) % times
    return numbers[answer]