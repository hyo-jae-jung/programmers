a,b = map(int,input().split())

import datetime as dt

def solution(a,b):
    weekday = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return weekday[dt.datetime(2016,a,b).weekday()]

if __name__ == "__main__":
    print(solution(a,b))
    