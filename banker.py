def is_safe_state(available, max_demand, allocation):
    n = len(max_demand)
    m = len(available)
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    work = available[:]
    safe_seq = []

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                safe_seq.append(i)
                finish[i] = True
                allocated = True
        if not allocated:
            return False, []

    return True, safe_seq

# Example usage:
available = [3, 3, 2]
max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

safe, seq = is_safe_state(available, max_demand, allocation)
print("Safe Sequence:", seq if safe else "Not Safe")
