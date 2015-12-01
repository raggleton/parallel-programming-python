from multiprocessing import Pool, cpu_count, current_process


def square(x):
    print("Worker %s calculating square of %d" % \
         (current_process().pid, x))
    return x*x


if __name__ == "__main__":
    nprocs = 2

    # print the number of cores
    print("Number of workers equals %d" % nprocs)

    # create a pool of workers
    pool = Pool(processes=nprocs)

    a = range(1, 5001)

    result = pool.map(square, a)

    total = reduce(lambda x,y: x+y, result)

    print 'The sum of the squares is ', total