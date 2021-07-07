def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        cat = [i for i in range(1,n+1)]

        if len(cat)%2 > 0:
            cat[0], cat[1], cat[2] = cat[2], cat[0], cat[1]
            if len(cat) > 3:
                for i in range(3, len(cat)-1, 2):
                    cat[i], cat[i + 1] = cat[i + 1], cat[i]
        else:
            for i in range(0, n-1, 2):
                cat[i], cat[i+1] = cat[i+1], cat[i]

        print(*cat)


if __name__ == '__main__':
    main()









