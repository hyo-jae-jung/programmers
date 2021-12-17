import math

def solution(w,h):

    total_block_count = h*w
    white_block_count = 0
    x = 1

    if h/w - int(h/w) == 0:
        white_block_count = h
    elif w/h - int(w/h) == 0:
        white_block_count = w
    else:
        for i in range(1,w+1):
            white_block_count += (math.ceil(i*h/w) - math.floor((i-1)*h/w))
            if i*h/w - int(i*h/w) == 0:
                x = int(w/i)
                break
        
    answer = total_block_count - white_block_count*x
    return answer

print(solution(3,5))
