def minimumTimeRequired(jobs, k):
    workers = [0]*k
    jobs.sort(reverse=True)
    result = sum(jobs)

    def backtrack(i):
        nonlocal result
        if i == len(jobs):
            result = min(result, max(workers))
            return

        seen = set()
        for j in range(k):
            if workers[j] not in seen:
                seen.add(workers[j])
                workers[j] += jobs[i]
                if workers[j] < result:
                    backtrack(i+1)
                workers[j] -= jobs[i]
            if workers[j] == 0:
                break

    backtrack(0)
    return result


# Test
print(minimumTimeRequired([1,2,4,7,8], 2))  # Output: 11
