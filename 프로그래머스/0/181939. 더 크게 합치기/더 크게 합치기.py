def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    if ba > ab:
        return ba
    else:
        return ab