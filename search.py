from __future__ import print_function
from collections import deque

def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == "__main__":
    with open('somefile.txt', 'r') as f:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline)
            # print(line)
            print('-' * 20)
