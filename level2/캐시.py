from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cities = deque(cities)
    for i in cities:
        i=i.lower()
        if i in cache:
            answer+=1
            cache.remove(i)
            cache.append(i)
        else:
            answer+=5
            cache.append(i)
            if len(cache) > cacheSize:
                cache.popleft()
    return answer

if __name__ == "__main__":
    print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
