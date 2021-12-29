def solution(numbers, hand):
    thumbs_location = {
        'left':[0,0],
        'right':[2,0]
    }
    buttons_location = {
        '*':[0,0],
        0:[1,0],
        '#':[2,0],
        7:[0,1],
        8:[1,1],
        9:[2,1],
        4:[0,2],
        5:[1,2],
        6:[2,2],
        1:[0,3],
        2:[1,3],
        3:[2,3]
    }
    answer = ''

    for i in numbers:

        if i in [3,6,9]:
            thumbs_location['right'] = buttons_location[i]
            answer += 'R'
        elif i in [1,4,7]:
            thumbs_location['left'] = buttons_location[i]
            answer += 'L'
        elif i in [2,5,8,0]:
            L_distance = abs(buttons_location[i][0]-thumbs_location['left'][0])+abs(buttons_location[i][1]-thumbs_location['left'][1])
            R_distance = abs(buttons_location[i][0]-thumbs_location['right'][0])+abs(buttons_location[i][1]-thumbs_location['right'][1])

            if L_distance<R_distance:
                thumbs_location['left'] = buttons_location[i]
                answer += 'L'
            elif L_distance>R_distance:
                thumbs_location['right'] = buttons_location[i]
                answer += 'R'
            elif L_distance == R_distance:
                thumbs_location[hand] = buttons_location[i]
                answer += hand[0].upper()

    return answer