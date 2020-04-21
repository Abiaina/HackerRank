def get_time_blocks (time_blocks):
    times = {}
    max_time = 0
    time_range_pairs = []
    for num_pair in time_blocks:
        start = num_pair[0]
        stop = num_pair[1]
        if stop > max_time:
            max_time = stop
        while start != stop:
            times[start] = 1
            start += 1
    num = 0
    while num < max_time + 1:
        if num in times:
            cur = num
            time_range_pair = [num]
            while cur in times:
                cur += 1
            time_range_pair.append(cur)
            time_range_pairs.append(time_range_pair)
            num = cur + 1
        else:
            num = num + 1
    for index,pair in enumerate(time_range_pairs):
        time_range_pairs[index] = (pair[0],pair[1])
    return(time_range_pairs)
        
         
# Tests
test_1 = get_time_blocks([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]
test_2 = get_time_blocks([(1, 3), (2, 4)]) == [(1, 4)]
test_3 = get_time_blocks([(1, 2), (2, 3)]) == [(1, 3)]
test_4 = get_time_blocks([(1, 5), (2, 3)]) == [(1, 5)]
test_5 = get_time_blocks([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
if not test_1 or not test_2 or not test_3 or not test_4 or not test_5:
    print("Fail")
else:
    print("All tests passing!!")

# Time complexity = O(3Cn) ---> O(n). Where C is the largest interview time's integer value (C could be larger or smaller than n).
# Space complexity = O(n)