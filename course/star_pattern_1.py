def main():
   
    n = int(input())
    x = n 
    for i in range(n):
        star = x
        space = n*2 - star*2
        while star > 0:
            print('*',end='')
            star -= 1
        star = x
        while space > 0:
            print(' ',end='')
            space -= 1
        while star > 0:
            print('*',end='')
            star -= 1
        x -= 1
        print()
    
    x = 1
    for i in range(n):
        star = x
        space = n*2 - star*2
        while star > 0:
            print('*',end='')
            star -= 1
        while space > 0:
            print(' ',end='')
            space -= 1
        star = x
        while star > 0:
            print('*',end='')
            star -= 1
        x += 1
        print()
    return 0

if __name__ == '__main__':
    main()