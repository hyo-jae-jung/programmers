sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    w,h = 0,0
    for i in sizes:
        i.sort()
        if w < i[0]:w = i[0]
        if h < i[1]:h = i[1]
    return w*h

if __name__ == "__main__":
    print(solution(sizes))