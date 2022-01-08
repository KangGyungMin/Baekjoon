import heapq
import sys
input = sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []

for i in range(N):
    x = int(input())
    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, x)

    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, x * -1)

    if min_heap and max_heap[0] * -1 > min_heap[0]:
        temp = heapq.heappop(max_heap) * -1
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
        heapq.heappush(min_heap, temp)

    print(max_heap[0] * -1)
