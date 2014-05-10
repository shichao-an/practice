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
    return h


if __name__ == '__main__':
    r1 = [8, 3, 4, 5, 1, 6, 7, 9, 2]
    k1 = 4
    print get_largest_k_numbers(r1, k1)
