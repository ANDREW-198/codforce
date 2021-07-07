def main():
    k = int(input())
    for i in range(k):
        n, x, t = map(int, input().split())
        dis = dis_count(n, x, t)
        print(dis)

def dis_count(n,x,t):
    if n == 1:
        return 0
    elif x < t:
        if t//x >= x*n:
            return (n*n + n)//2
        else:
            i = n - t//x
            return t//x * (n - t//x) + (i*i + i)//2

        pass
    elif x > t:
        return 0
    elif x == t:
        return n-1
    else:
        print('WTF')

def test():
    test_ans = (
        ((4, 2, 5,), 5),
        ((3, 1, 2), 3),
        ((3, 3, 10), 3),
        ((2000000000, 1, 2000000000), 1999999999000000000),
        ((1, 1, 100), 0),
        ((1, 1, 1), 0),
        ((2, 2, 2), 1),
        ((5, 1, 3), 9)
        )

    for index, i in enumerate(test_ans):
        if dis_count(i[0][0], i[0][1], i[0][2]) == i[1]:
            print('test_{} is OK'.format(index))
        else:
            print('test_{} is FAIL, dis={})'.format(index, dis_count(i[0][0], i[0][1], i[0][2])))


if __name__ == '__main__':
    test()
    pass
    main()
