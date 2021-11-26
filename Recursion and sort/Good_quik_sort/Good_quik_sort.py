# 59225666
def partition(array, left, right):
    pivot = array[(left + right) // 2]
    lf = left - 1
    rg = right + 1

    while True:
        lf += 1
        while array[lf] < pivot:
            lf += 1

        rg -= 1
        while array[rg] > pivot:
            rg -= 1

        if lf >= rg:
            return rg

        array[lf], array[rg] = array[rg], array[lf]


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid)
        quick_sort(array, mid + 1, right)

    return array


def main():
    n = int(input())
    participants = []
    for _ in range(n):
        name, right_task, penalty = input().split()
        participants.append([-int(right_task), int(penalty), name])

    quick_sort(participants, 0, len(participants) - 1)
    result = "\n".join([participant[2] for participant in participants])
    print(result)


if __name__ == '__main__':
    main()
