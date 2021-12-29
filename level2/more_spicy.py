import heapq

def solution(scoville, K):
    answer = -1
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    temp_answer = 0
    while len(heap) > 0:
        if heap[0] < K:
            if len(heap) > 1:
                temp = heap[0]
                heapq.heappop(heap)
                temp += heap[0]*2
                heapq.heappop(heap)
                heapq.heappush(heap,temp)
                temp_answer += 1
            else:
                heapq.heappop(heap)
        else:
            answer = temp_answer
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12]	,7))