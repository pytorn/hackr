l = []         
with open(' address ', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append(list(map(int, line.split(','))))