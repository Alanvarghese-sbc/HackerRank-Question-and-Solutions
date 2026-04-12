
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    unq_arr = list((set(arr)))
    unq_arr.sort()
    print(unq_arr[-2])
    

or

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(sorted(set(arr))[-2]) 
