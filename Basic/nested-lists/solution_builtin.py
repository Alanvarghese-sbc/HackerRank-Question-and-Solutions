if __name__ == '__main__':
    
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    second_lowest = sorted(list(set(score for name,score in students)))[1]
    
    names = [name for name, score in students if score == second_lowest ]    
    names.sort()
    
    for name in names:
        print(name)
