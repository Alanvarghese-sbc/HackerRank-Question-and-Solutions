def split_and_join(line):
    words = line.split(" ")
    
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += "-"
    
    return result

if __name__ == '__main__':
    line = input()
    print(split_and_join(line))
