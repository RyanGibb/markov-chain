
import sys

dictionary = {}

def train(data, order = 1):
    for i in range(len(data) - order):
        key = data[i:i+order]
        if key not in dictionary:
            dictionary[key] = {}
        next_key = data[i+order:i+order*2]
        if next_key not in dictionary[key]:
            dictionary[key][next_key] = 1
        else:
            dictionary[key][next_key] += 1


def generate():
    pass


if __name__ == "__main__":
    train(sys.stdin.readlines())
    generate()
