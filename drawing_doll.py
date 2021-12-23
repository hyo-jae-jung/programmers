def solution(board, moves):
    answer = 0

    basket = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
    i = 0
    while i < len(basket)-1:
        if basket[i] == basket[i+1]:
            answer += 2
            del basket[i:i+2]
            i = 0
        else:
            i += 1

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))