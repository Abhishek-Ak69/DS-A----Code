def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    # sort the array
    a.sort()
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1

    # find longest sequence
    for i in range(n):
        if a[i] - 1 == lastSmaller:
            # a[i] is the next element of the
            # current sequence
            cnt += 1
            lastSmaller = a[i]
        elif a[i] != lastSmaller:
            cnt = 1
            lastSmaller = a[i]
        longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)
