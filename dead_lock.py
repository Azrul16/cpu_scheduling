def detect_deadlock(allocation, request, available):
    n = len(allocation)
    m = len(available)
    work = available[:]
    finish = [False] * n

    while True:
        progress = False
        for i in range(n):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                progress = True
        if not progress:
            break

    return not all(finish)

# Example
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
request = [[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
available = [0, 0, 0]

print("Deadlock Detected" if detect_deadlock(allocation, request, available) else "No Deadlock")
