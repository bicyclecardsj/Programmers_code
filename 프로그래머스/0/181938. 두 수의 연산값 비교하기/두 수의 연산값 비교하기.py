def solution(a, b):
    answer1 = int(str(a) + str(b))
    answer2 = 2 * a * b
    if answer2 > answer1:
        answer = answer2
    else:
        answer = answer1
    
    return answer