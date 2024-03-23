import heapq
import sys

N = int(sys.stdin.readline())
mid = int(sys.stdin.readline())

print(mid)

l_max_heap = []
r_min_heap = []

for _ in range(N - 1):
    num = int(sys.stdin.readline())

    if num > mid:
        heapq.heappush(r_min_heap, num)
        if len(l_max_heap) + 1 < len(r_min_heap):
            heapq.heappush(l_max_heap, -mid)
            mid = heapq.heappop(r_min_heap)

    else:
        heapq.heappush(l_max_heap, -num)
        if len(r_min_heap) < len(l_max_heap):
            heapq.heappush(r_min_heap, mid)
            mid = -heapq.heappop(l_max_heap)

    # if mid < num:
    #     heapq.heappush(r_min_heap, num)
    #     if len(r_min_heap) - len(l_max_heap) == 2:
    #         heapq.heappush(l_max_heap, -mid)
    #         mid = heapq.heappop(r_min_heap)
    # else:
    #     heapq.heappush(l_max_heap, -num)
    #     if len(l_max_heap) - len(r_min_heap) == 1:
    #         heapq.heappush(r_min_heap, mid)
    #         mid = -heapq.heappop(l_max_heap)

    print(mid)
