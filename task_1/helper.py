def read_file(filename):
    out = []
    file = open(filename, 'r')
    for line in file:
        out += [float(x) for x in line.split()]
    return out
