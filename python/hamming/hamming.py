def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('strands must be of equal length')
    hamming = 0
    for i,v in enumerate(strand_a):
        hamming += 1 if v != strand_b[i] else 0
    return hamming

