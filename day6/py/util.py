def is_unique(seq):
    return len(set(seq)) == len(seq)

def find_unique_sequence(f, length):

    sop = f.read(length)

    chars_read = length

    if not is_unique(sop):
        for char in f.readline():
            chars_read += 1

            sop = sop[1:] + char

            if is_unique(sop):
                break

    return chars_read
