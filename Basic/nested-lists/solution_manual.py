
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find lowest score
    lowest = students[0][1]
    for student in students:
        if student[1] < lowest:
            lowest = student[1]

    # Find second lowest
    second_lowest = None
    for student in students:
        score = student[1]
        if score != lowest:
            if second_lowest is None or score < second_lowest:
                second_lowest = score

    # Collect names
    names = []
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    # Manual sort (Bubble Sort)
    for i in range(len(names)):
        for j in range(0, len(names) - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]

    # Print
    for name in names:
        print(name)
