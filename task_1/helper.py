def read_file(filename):
    out = []
    file = open(filename + '.txt', 'r')
    for line in file:
        out += [float(x) for x in line.split()]
    return out
