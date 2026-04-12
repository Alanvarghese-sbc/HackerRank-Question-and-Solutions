
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = arr[0]
    
    for i in arr:
        if i > max_val:
            max_val = i
    
    second_max = None
    
    for i in arr:
        if i != max_val:
            if second_max is None or i > second_max:
                second_max = i
            
            
    print(second_max)
