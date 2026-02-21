def solution(spell, dic):
    spell.sort()
    
    for word in dic:
        word_sorted = sorted(word)
        
        if spell == word_sorted:
            return 1
    return 2
