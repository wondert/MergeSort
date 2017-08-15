e = list(range(15))
f = list(range(1,13))
g = list(range(1,12))

def splitter(randomseq, blocks=2):
    static_length = len(randomseq)
    block_size = static_length//blocks
    start = 0
    stop = block_size
    for block in range(blocks):
        if stop < static_length:
            yield randomseq[start:stop]
        start += block_size
        stop += start
    yield randomseq[start:]


print(list(splitter(g)))

'''
This is ultimately not how we want to split. Just example use with generators.
Would result in merged giveing the following result:
[1,6,11,2...]
rather than
[1,6,2,7...11]
'''
