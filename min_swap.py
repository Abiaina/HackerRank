def minimumSwaps(arr):
    swaps = 0
    visited = {}
    visiting = []
    for index, num in enumerate(arr):
        if num == index:
            visited[num] = "visited"
        elif num not in visited:
            unordered_index = index
            unordered_num = num
            while unordered_num != unordered_index:
                print(unordered_num)
                if unordered_num in visiting:
                    print(visiting)
                    swaps += len(visiting) -1
                    break
                unordered_num = arr[unordered_num]
                unordered_index = unordered_num
                visited[unordered_num] = "visited"
                visiting.append(unordered_num)
                # print(visiting)
            visiting = []
        # print(visited)
    return swaps

print(minimumSwaps([0,2,3,1,5,4]))