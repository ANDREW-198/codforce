def main():
    t = int(input())
    for i in range(t):
        _ = input()
        Number = list(map(int, input().split()))
        print(count(Number))


def count(Number):
    even, odd = 0, 0
    for i in Number:
        if i%2 > 0:
            odd += 1
        else:
            even += 1
    if even == odd:
        return 'YES'
    else:
        return 'NO'


def test():

    if count([2, 3, 4, 5]) == 'YES':
        print('TEST 01 is OK')
    else:
        print('TEST 01 is FAIL!!!')

    if count([2, 3, 4, 5, 5, 5]) == 'NO':
        print('TEST 02 is OK')
    else:
        print('TEST 02 is FAIL!!!')

    if count([2, 4]) == 'NO':
        print('TEST 03 is OK')
    else:
        print('TEST 03 is FAIL!!!')

    if count([2, 3]) == 'YES':
        print('TEST 04 is OK')
    else:
        print('TEST 04 is FAIL!!!')

    if count([1, 5, 3, 2, 6, 7, 3, 4]) == 'NO':
        print('TEST 02 is OK')
    else:
        print('TEST 02 is FAIL!!!')


if __name__ == "__main__":
    main()
    #test()


































