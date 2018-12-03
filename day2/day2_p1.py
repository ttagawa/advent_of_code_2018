from collections import Counter

def get_checksum():
    cs_helper_dict = {2: 0, 3: 0}
    with open('input_p1.txt', 'r') as f:
        for id in f:
            char_dict = Counter(id.strip())
            has_trips = 0
            has_dubs = 0
            for k, v in char_dict.items():
                if has_dubs and has_trips:
                    break
                if v == 2:
                    has_dubs = 1
                elif v == 3:
                    has_trips = 1
            cs_helper_dict[2] += has_dubs
            cs_helper_dict[3] += has_trips
    return cs_helper_dict[2] * cs_helper_dict[3]

if __name__ == '__main__':
    checksum = get_checksum()
    print(checksum)