"""The merged module implements the mergesort algorithm."""

from dupsort import recursivesort


def merged(*sequences):
    """Merge n sequences into single sequence iteratively by index."""
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
    """Splits a sequence into n blocks. returns a tuple of n lists."""
    # TODO refactor to a generator function
    # split sequence into n blocks of equal size
    if len(reseq) % blocks == 0:
        block_size = len(reseq)//blocks
        index = 0
        sections = []
        for _ in range(blocks):
            sections.append(reseq[index:index+block_size])
            index += block_size
        return tuple(item for item in sections)
    # split sequence into n blocks
    # remaining items are sequentially split between blocks
    else:
        block_size = len(reseq)//blocks
        index = 0
        sections = []
        last_piece = []
        for _ in range(blocks):
            try:
                sections.append(reseq[index:index+block_size])
                index += block_size
            except IndexError:
                break
        if index != len(reseq):
            for item in range(index, index+block_size-1):
                try:
                    last_piece.append(reseq[item])
                except IndexError:
                    pass
            for i in range(len(last_piece)):
                sections[i].append(last_piece[i])
        return tuple(item for item in sections)


def generic_splitsort(randomseq, blocks=2, key=None, reverse=False):
    """Splits a sequence into n blocks, recursively sorts, then merges."""
    # TODO refactor into generic sorting function that handles n sequences.
    if key:
        # generate mappings to recall original index, keys, values
        keyedseq = [(key(element), index)
                    for index, element in enumerate(randomseq)]

        # split keyed sequence into n blocks
        # TODO - does splitseq work with keyedseq tuple elements???
        kseq = splitseq(keyedseq, blocks)

        # set globals to track value swaps
        switch = 0
        compares = 0
        flip = 1

        # setup infinite loop
        while True:
            # recursively sort each sequence
            if flip:     # Case1 - ensure the first sort
                sortedseq = []
                for index, item in enumerate(kseq):
                    seq, switch = recursivesort(item)
                    sortedseq.append(seq)
                    compares += switch
                # TODO - check if statement below gives expected result...
                # TODO - since seq is actually a tuple
                reseq = merged(*tuple(element for element in sortedseq))
                kseq = splitseq(reseq, blocks)
                flip = 0

            elif compares:       # Case2 - keep sorting if last loop had sorts
                compares = 0
                sortedseq = []
                for index, item in enumerate(kseq):
                    seq, switch = recursivesort(item)
                    sortedseq.append(seq)
                    compares += switch
                # TODO - check if statement below gives expected result...
                # TODO - since seq is actually a tuple
                reseq = merged(*tuple(element for element in sortedseq))
                kseq = splitseq(reseq, blocks)

            else:               # Case3 - no sorts
                break

        # recover keyed elements and create sorted sequence
        # seq1 = [randomseq[seq1[element][1]] for element in range(len(seq1))]
        # TODO - make a generic function to do the procedure above
        # TODO - can we just use merged then recover all elements? YES!!!
        seq_keyed = merged(*kseq)
        kseq = [randomseq[seq_keyed[element][1]]
                for element in range(len(seq_keyed))]

    else:
        # split sequence into n blocks
        kseq = splitseq(randomseq, blocks)

        # set globals to track value swaps
        switch = 0
        compares = 0
        flip = 1

        # setup infinite loop
        while True:
            # recursively sort each sequence
            if flip:     # Case1 - ensure the first sort
                sortedseq = []
                for index, item in enumerate(kseq):
                    seq, switch = recursivesort(item)
                    sortedseq.append(seq)
                    compares += switch
                reseq = merged(*tuple(element for element in sortedseq))
                kseq = splitseq(reseq, blocks)
                flip = 0

            elif compares:       # Case2 - keep sorting if last loop had sorts
                compares = 0
                sortedseq = []
                for index, item in enumerate(kseq):
                    seq, switch = recursivesort(item)
                    sortedseq.append(seq)
                    compares += switch
                reseq = merged(*tuple(element for element in sortedseq))
                kseq = splitseq(reseq, blocks)

            else:               # Case3 - no sorts
                break

        seq = merged(*kseq)

    # combine sorted sequences, check if reverse, and return sorted sequence
    seq = merged(*kseq)
    if reverse:
        seq.reverse()
    return seq


def splitsort(randomseq, key=None, reverse=False):
    """Splits a sequence into two blocks, recursively sorts, then merges."""
    if key:
        # generate mappings to recall original index, keys, values
        keyedseq = [(key(element), index)
                    for index, element in enumerate(randomseq)]

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

    else:
        # TODO refactor above for non-keyed sequence
        pass

    # combine sorted sequences, check if reverse, and return sorted sequence
    seq = seq1 + seq2
    if reverse:
        seq.reverse()
    return seq
