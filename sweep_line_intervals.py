import sys

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    t_len = int(input_data[1])

    events = []

    for i in range(2, 2 * n + 1, 2):
        start_pos = int(input_data[i])
        end_pos = int(input_data[i + 1])

        events.append((start_pos, 0))
        events.append((end_pos, 1))

    events.sort()

    current_snow = 0
    max_snow = 0
    best_pos = 0

    for pos, event_type in events:
        if event_type == 0:
            current_snow += 1
            
            if current_snow > max_snow:
                max_snow = current_snow
                best_pos = pos
        else:
            current_snow -= 1

    print(f"{max_snow} {best_pos}")

if __name__ == "__main__":
    main()
