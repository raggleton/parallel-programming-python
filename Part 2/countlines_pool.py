import os, sys
from multiprocessing import Pool
import contextlib

def count_lines(filename):
    return len(open(filename).readlines())


if __name__ == "__main__":
    files = [os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1])
             if f != "README"]
    with contextlib.closing(Pool()) as pool:
        line_counts = pool.map(count_lines, files)
    for f, lc in zip(files, line_counts):
        print f, '=', lc
    total = reduce(lambda x,y: x+y, line_counts)
    print 'Total:', total