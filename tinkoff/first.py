def manufactor(silver, blank, monet, count):
    if silver // blank == 0:
        return count
    currency = (blank // monet) * silver // blank
    count += currency
    silver += (blank % monet) * (silver // blank) - (silver // blank) * blank
    return manufactor(silver, blank, monet, count)


if __name__ == '__main__':
    n, k, m = map(int, input().split())
    print(manufactor(n, k, m, count=0))
