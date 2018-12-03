import re
from collections import defaultdict

def parse_claim(claim):
    nums = list(map(int, re.findall(r'\d+', claim)))
    dimensions = {
        'claim_id': nums[0],
        'x': nums[1],
        'y': nums[2],
        'width': nums[3],
        'height': nums[4]
    }
    return dimensions

def create_key(x, y):
    return "{x}x{y}".format(x=x, y=y)

def build_overlap_dict():
    overlap_dict = defaultdict(int)
    with open('input.txt', 'r') as f:
        for claim in f:
            dim = parse_claim(claim)
            for x in range(dim['x'], dim['x'] + dim['width']):
                for y in range(dim['y'], dim['y'] + dim['height']):
                    key = create_key(x,y)
                    overlap_dict[key] += 1
    return overlap_dict

def calculate_overlap_sq_in():
    overlap_dict = build_overlap_dict()
    overlap = 0
    for v in overlap_dict.values():
        if v > 1:
            overlap += 1
    return overlap

if __name__ == '__main__':
    overlap = calculate_overlap_sq_in()
    print(overlap)
