def set_parity(value):
    mid = sum(value)/10
    count = 0
    while len(set(value)) != 1:
        count += 1
        max_value = max(value)
        value[value.index(max_value)] = mid
        dif = max_value - mid
        i = 0
        while dif != 0:
            if value[i] < mid:
                odds = mid - value[i]
                if dif >= odds:
                    dif -= odds
                    value[i] = mid
                else:
                    value[i] += dif
                    dif = 0
            i += 1
    return count


if __name__ == '__main__':
    cups = 10
    value = []
    while cups != 0:
        cups -= 1
        value.append(int(input()))
    print(set_parity(value))
