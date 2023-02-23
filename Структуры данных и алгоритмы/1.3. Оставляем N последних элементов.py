from collections import deque

# deque(maxlen=N) создает очередь фиксированной длины
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open('somefile.txt') as f:
    for line, prevlines in search(f, 'Python', 5):
        for pline in prevlines:
            print(pline, end='')
        # print(line, end='')
        print('-' * 20)
