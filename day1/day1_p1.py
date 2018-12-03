def get_frequency():
    with open('input.txt', 'r') as f:
        freq = 0
        while True:
            line = f.readline()
            if not line:
                break
            freq += int(line.strip())
        return freq

if __name__ == '__main__':
    freq = get_frequency()
    print(freq)