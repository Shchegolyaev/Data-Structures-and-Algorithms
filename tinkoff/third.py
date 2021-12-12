def f(a, n, p, variables):
    if n:
        for i in range(n + 1, 0, -1):
            if i <= p:
                array = f(a + [i], n - i, i, variables)
                if not n-i:
                    if len(array) == 2:
                        array.append(0)
                        variables.append(array)
                    elif len(array) == 3:
                        variables.append(array)
                    elif len(array) == 1:
                        array.append(0)
                        array.append(0)
                        variables.append(array)
        return variables
    else:
        return a


def count_combination(bank):
    count = 0
    for element in bank:
        if len(set(element)) == 2:
            count += 18
        if len(set(element)) == 3:
            count += 36
    return count


if __name__ == '__main__':
    n = int(input())
    bank = f([], n, n, variables=[])
    print(bank)
    if len(bank) != 0:
        print(count_combination(bank))
    else:
        print(1)
