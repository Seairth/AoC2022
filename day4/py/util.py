def get_range_pair(line):
    comma = line.find(',')
    dash1 = line.find('-', 0, comma)
    dash2 = line.find('-', comma)

    r1_min = int(line[:dash1])
    r1_max = int(line[dash1+1:comma])

    r2_min = int(line[comma+1:dash2])
    r2_max = int(line[dash2+1:])

    return ((r1_min, r1_max), (r2_min, r2_max))

def contains(range_1, range_2):
    return range_1[0] <= range_2[0] and range_1[1] >= range_2[1]

def overlaps(range_1, range_2):
    return contains(range_1, (range_2[0], range_2[0])) or contains(range_2, (range_1[0], range_1[0]))