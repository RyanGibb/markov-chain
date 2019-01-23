import random
import sys

dictionary = {}


def train(data, order=1):
    for i in range(len(data) - order):
        key = data[i:i+order]
        if key not in dictionary:
            dictionary[key] = {}
        next_key = data[i+order:i+order*2]
        if next_key not in dictionary[key]:
            dictionary[key][next_key] = 1
        else:
            dictionary[key][next_key] += 1


def generate(output, max_num_events=-1):
    f = open(output, 'wb')
    last_event = random.choice(list(dictionary))
    num_events = 0
    while num_events != max_num_events:
        if last_event not in dictionary:
            last_event = random.choice(list(dictionary))
            f.write(last_event)
            num_events += 1
        next_events = dictionary[last_event]
        last_event = get_next_event(next_events)
        f.write(last_event)
        num_events += 1
    f.close()


def get_next_event(next_events):
    total_occurrences = 0
    for occurrences in next_events.values():
        total_occurrences += occurrences
    sum = 0
    rand_val = random.randint(0, total_occurrences)
    for next_event, occurrences in next_events.items():
        sum += occurrences
        if rand_val <= sum:
            return next_event


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("No number of events to generate input. Default value of infinity (-1) used")
        max_num_events = -1
    else:
        max_num_events = int(sys.argv[2])
    if len(sys.argv) < 2:
        print("No order input. Default value of 1 used.")
        print("Usage: python markov_chain.py <order> <number of events to generate>")
        order = 1
    else:
        order = int(sys.argv[1])
    train("".join(sys.stdin.readlines()), order)
    print()
    generate(max_num_events)
