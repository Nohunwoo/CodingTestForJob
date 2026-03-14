def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    