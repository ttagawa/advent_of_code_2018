from day3_p1 import parse_claim, create_key, build_overlap_dict

def is_non_overlapping(claim_info, overlap_dict):
    for x in range(claim_info['x'], claim_info['x'] + claim_info['width']):
        for y in range(claim_info['y'], claim_info['y'] + claim_info['height']):
            key = create_key(x,y)
            if overlap_dict[key] > 1:
                return False
    return True

def find_non_overlapping_claim():
    overlap_dict = build_overlap_dict()
    with open('input.txt', 'r') as f:
        for claim in f:
            claim_info = parse_claim(claim)
            if is_non_overlapping(claim_info, overlap_dict):
                return claim_info['claim_id']
    return -1

if __name__ == '__main__':
    non_overlapping_claim = find_non_overlapping_claim()
    print(non_overlapping_claim)
