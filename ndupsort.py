"""The ndupsort module contains functions to recursively sort a sequence.

This module is an expansion upon the dupsort recursivesort function. It is
compatible with sequences that contain duplicate values. recursivesort will
retain duplicate values in their original order in the unsorted sequence.
"""

# test sequences for validation of sorting
unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81]
unsorted2 = ['sixteen', 'one', 'eighteen', 'seven', 'five', 'twelve']
dupseq1 = [29, 15, 32, 1, 7, 72, 35, 7, 81]
dupseq2 = ['sixteen', 'one', 'six', 'seven', 'five', 'twelve']

# TODO - add * in params to force specifying keywords
# TODO - new API will break inner function calls due to recursion!!!
def recursivesort(sequence, slidingstart=0, switch=0):
    """Recursively sort a sequence to shift the higher value right.

    recursivesort takes three arguments, and returns a tuple containing the
    sorted sequence with the highest value shifted to the right end and a
    flag, switch, which indicates if any value shifted during the function
    call.

    recursivesort in the dupsort module can take a sequence of tuples or
    a sequence of values as in the popsort module. If the sequence contains
    tuples, they will be sorted based upon their value at index 0.

    # TODO - make changes to API and documentation
    recursivesort in the ndupsort module has been further modified to ...

    recursivesort(mutable sequence, int, int) -> mutated sequence, int

    :param sequence: container with elements to sort.
    :type sequence: mutable sequence; list or dict. must support .insert.
    :param slidingstart: (optional) index to start right shifting values.
    :type slidingstart: int, default = 0.
    :param switch: (optional) flag to indicate if function shifted a value.
    :type switch: int, default=0.
    """
    # check if sequence is list of tuples.
    if isinstance(sequence[0], tuple):
        # return sequence once final two values compared
        if not (len(sequence) - slidingstart - 1):
            return sequence, switch

        # right shift larger value if it is to the left in the sequence
        elif sequence[slidingstart][0] > sequence[slidingstart+1][0]:
                sequence[slidingstart], sequence[slidingstart+1] = (
                    sequence[slidingstart+1], sequence[slidingstart])
                switch = 1
                return recursivesort(sequence, slidingstart+1, switch)

            # recursive call to the next value in sequence
        else:
            return recursivesort(sequence, slidingstart+1, switch)

    else:
        # return sequence once final two values compared
        if not (len(sequence) - slidingstart - 1):
            return sequence, switch

        # right shift larger value if it is to the left in the sequence
        elif sequence[slidingstart] > sequence[slidingstart+1]:
                sequence[slidingstart], sequence[slidingstart+1] = (
                    sequence[slidingstart+1], sequence[slidingstart])
                switch = 1
                return recursivesort(sequence, slidingstart+1, switch)

            # recursive call to the next value in sequence
        else:
            return recursivesort(sequence, slidingstart+1, switch)
