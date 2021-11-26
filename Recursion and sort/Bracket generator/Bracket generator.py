def gen_brackets(string, left, right, pairs):
    if left == pairs and right == pairs:
        print(string)
    else:

        if left < pairs:
            gen_brackets(string + '(', left + 1, right, pairs)

        if right < left:
            gen_brackets(string + ')', left, right + 1, pairs)


def main():
    pair_brackets = int(input())
    gen_brackets('', 0, 0, pair_brackets)


if __name__ == '__main__':
    main()