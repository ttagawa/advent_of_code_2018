import re
from collections import defaultdict

def get_id(str):
    match = re.search(r'#(\d+)', str)
    return match.group(1)

def parse_file():
    with open('input.txt', 'r') as f:
        content = sorted([line.strip() for line in f.read().splitlines()])
        return content

def parse_minutes(str):
    match = re.search(r'\d{2}:(\d{2})', str)
    minutes = match.group(1)
    if minutes.startswith('0'):
        minutes = minutes[1:]
    return int(minutes)

def build_sleep_dict(time_log):
    curr_guard = get_id(time_log[0])
    sleep_start = None
    sleep_dict = {}
    for log in time_log:
        if 'Guard' in log:
            curr_guard = get_id(log)
            if curr_guard not in sleep_dict:
                sleep_dict[curr_guard] = defaultdict(int)
        if 'falls' in log:
            sleep_start = parse_minutes(log)
        if 'wakes' in log:
            sleep_end = parse_minutes(log)
            if sleep_start is None:
                raise ValueError('wake found before sleep for guard: {}'.format(curr_guard))
            for minute in range(sleep_start, sleep_end):
                sleep_dict[curr_guard][minute] += 1
    return sleep_dict
        
def build_total_sleep_dict(sleep_dict):
    total_sleep_dict = defaultdict(int)
    for k, v in sleep_dict.items():
        total_sleep_dict[k] = sum(v.values())
    return total_sleep_dict

def calculate_answer(sleep_dict, total_sleep_dict):
    sleepiest_guard = None
    max_sleep = 0
    for k, v in total_sleep_dict.items():
        if v >= max_sleep:
            max_sleep = v
            sleepiest_guard = k
    most_common_minute = None
    max_occurence_count = 0
    for k, v in sleep_dict[sleepiest_guard].items():
        if v >= max_occurence_count:
            max_occurence_count = v
            most_common_minute = k
    return int(sleepiest_guard) * most_common_minute

if __name__ == '__main__':
    time_log = parse_file()
    sleep_dict = build_sleep_dict(time_log)
    total_sleep_dict = build_total_sleep_dict(sleep_dict)
    answer = calculate_answer(sleep_dict, total_sleep_dict)
    print(answer)