def min_pool(pool:list)->int:
    return pool.index(min(pool))


def queue_time(customers, n):
    if customers == []:
        return 0
    pool = [[0] for _ in range(min(n,len(customers)))]
    while len(customers) > 0:
        pool[min_pool(pool)][0] += customers.pop(0)

    return max(pool)[0]

def main():
    print(queue_time([2,3,10], 2))

main()
