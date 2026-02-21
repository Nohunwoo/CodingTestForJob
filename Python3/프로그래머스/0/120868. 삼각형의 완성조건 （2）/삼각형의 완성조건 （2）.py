def solution(sides):
    answer = 0
    for i in range(max(sides)+1):
        if max(sides)-min(sides) < i <= max(sides):
            answer += 1
    for i in range(max(sides)+1, sides[0]+sides[1]):
        answer += 1
    return answer

# 생각에는 범위가 2개여야함
# sides[0]과 sides[1]중에 작은것부터 큰것 사이의 범위 하나
# sides[0], sides[1] 둘중에 큰게 앞범위, 둘을 합친게 뒷범위
# 그런데 문제가 1,2일때 값은 둘다 2로 하나가 들어가야 맞지만
# 실제로 정한 범위에서는 앞은 1이고 뒤는 2가 나옴
# 3번째 예시도 또 다름
# 7~11일때 범위는 5~11로 7개, 11~18일때 12~17로 6개여야하지만
# 실제로는 4개 7개로 11개가 나옴