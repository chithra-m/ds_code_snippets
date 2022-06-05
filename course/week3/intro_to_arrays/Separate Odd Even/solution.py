def main():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int,(input().split())))
        list_odd = []
        list_even = []
        for i in a:
            if i % 2 == 0:
                list_even.append(i)
            else:
                list_odd.append(i)
        for i in list_odd:
            print(i,end=" ")
        print()
        for i in list_even:
            print(i,end=" ")
        print()

        t -=1
        
    return 0

if __name__ == '__main__':
    main()