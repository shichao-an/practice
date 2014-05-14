import heapq


def get_largest_k_numbers(nums, k):
    h = []
    for c in nums:
        if len(h) < k:
            heapq.heappush(h, c)
        else:
            min_c = heapq.heappop(h)
            if c > min_c:
                heapq.heappush(h, c)
            else:
                heapq.heappush(h, min_c)
    return [heapq.heappop(h) for i in range(len(h))]


def get_smallest_k_numbers(nums, k):
    h = []
    for c in nums:
        print h
        if len(h) < k:
            heapq.heappush(h, (-c, c))
        else:
            key, max_c = heapq.heappop(h)
            if c < max_c:
                heapq.heappush(h, (-c, c))
            else:
                heapq.heappush(h, (key, max_c))
    return [heapq.heappop(h)[1] for i in range(len(h))]


if __name__ == '__main__':
    r1 = [8, 3, 4, 5, 11, 6, 7, 9, 2]
    k1 = 4
    print get_largest_k_numbers(r1, k1)
    print get_smallest_k_numbers(r1, k1)
