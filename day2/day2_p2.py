def find_prototype():
    with open('input.txt', 'r') as f:
        ids = [line.strip() for line in f.readlines()]
        for curr in ids:
            for comparand in ids:
                diffs = 0
                for i in range(len(curr)):
                    if curr[i] != comparand[i]:
                        diffs += 1
                    if diffs > 1:
                        break
                if diffs == 1:
                    answer = ''
                    for i in range(len(curr)):
                        if curr[i] == comparand[i]:
                            answer += curr[i]
                    return answer

if __name__ == '__main__':
    prototype = find_prototype()
    print(prototype)