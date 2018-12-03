def get_repeated_freq():
    freq_map = {}
    freq = 0
    with open('input_p2.txt', 'r') as f:
        freq_changes = [int(line.strip()) for line in f.readlines()]
        while True:
            for change in freq_changes:
                freq += change
                if freq in freq_map:
                    return freq
                else:
                    freq_map[freq] = 1

if __name__ == '__main__':
    repeat = get_repeated_freq()
    print(repeat)
