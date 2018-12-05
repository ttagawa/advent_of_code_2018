from day4_p1 import build_sleep_dict, parse_file

def calculate_answer(sleep_dict):
    guard_with_consistent_sleep_schedule = None
    most_slept_on = None
    max_occurences = 0
    for guard, minute_counter in sleep_dict.items():
        for k, v in minute_counter.items():
            if v > max_occurences:
                max_occurences = v
                most_slept_on = k
                guard_with_consistent_sleep_schedule = guard
    return int(guard_with_consistent_sleep_schedule) * most_slept_on

if __name__ == '__main__':
    time_log = parse_file()
    sleep_dict = build_sleep_dict(time_log)
    answer = calculate_answer(sleep_dict)
    print(answer)