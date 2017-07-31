"""Test suite for the MergeSort module."""

import merged as md

# test sequences
a = [1,4,7,10]
b = [2,5,8,11]
c = [3,6,9,12]
d = [3,6,9]
e = list(range(15))
f = list(range(1,13))
g = list(range(1,12))

# tests for merged
assert md.merged(a, b, c) == f
print('md.merged produced {0} from {1}, {2}, {3}'.format(f, a, b, c))
assert md.merged(a, b, d) == g
print('md.merged produced {0} from {1}, {2}, {3}'.format(g, a, b, d))
# tests for splitseq
print(md.splitseq(g, blocks=4))
# md.splitseq()
