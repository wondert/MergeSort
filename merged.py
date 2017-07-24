'''The merged module implements the mergesort algorithm.'''

from dupsort import recursivesort,


def merged(*sequences):
    '''merge n sequences into single sequence iteratively by index.'''
    # build new sequnce from n blocks. blocks not required to be same length.
    static_length = len(sequences[0])
    mergedsequence = []
    index = 0
    while True:
        for element in sequences:
            try:
                mergedsequence.append(element[index])
            except IndexError:
                break
        index += 1
        if static_length == index:
            break

    return mergedsequence


def splitseq(reseq, blocks=2):
    '''splits a sequence into n blocks of equal size'''
    # split sequence into n blocks

    # assign those blocks to a tuple, splitseqs, with seqX as name.

    return splitseqs


def splitsort(randomseq, key=None, reverse=False):
    '''splitsort splits a sequence in half, recursively sorts, then merges.'''

    # consider refactoring into generic functions to handle n sequences.
    if key:
        # generate mappings to recall original index, keys, values
        keyedseq = [(key(element), index)
                    for index, element in enumerate(randomseq)]
        # maybe come up with a function to do this step...
        seq1 = keyedseq[:len(keyedseq)//2]
        seq2 = keyedseq[(len(keyedseq)//2):]

        # set globals to track value swaps
        switch1 = 0
        switch2 = 0
        compares = 0
        flip = 1

        # setup infinite loop
        while True:
            # recursively sort each sequence
            compares = switch1 + switch2
            # TODO - make a function to recursivesort n sequences as below
            if flip:     # Case1 - ensure the first sort
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)
                reseq = merged(seq1, seq2)
                seq1, seq2 = splitseq(reseq, blocks=2)
                flip = 0

            elif compares:       # Case2 - keep sorting if last loop had sorts
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)
                reseq = merged(seq1, seq2)
                seq1, seq2 = splitseq(reseq, blocks=2)

            else:               # Case3 - no sorts
                break

        # recover keyed elements and create sorted sequence
        seq1 = [randomseq[seq1[element][1]] for element in range(len(seq1))]
        seq2 = [randomseq[seq2[element][1]] for element in range(len(seq2))]
        # TODO - make a function to do the procedure above

    else:
        # DO STUFF

    # combine sorted sequences, check if reverse, and return sorted sequence
    seq = seq1+seq2
    if reverse:
        seq.reverse()
    return seq
