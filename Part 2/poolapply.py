from multiprocessing import Pool, current_process
import contextlib 
import time

def slow_sum( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then returns the sum of x and y"""
    print("Process %s going to sleep for %d second(s)" \
              % (current_process().pid,nsecs))

    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return x+y

if __name__ == "__main__":
    print("Master process is PID %d" % current_process().pid)

    with contextlib.closing( Pool() ) as pool:
        r = pool.apply( slow_sum, [1,6,7] )

    print("Result is %s" % r)