from multiprocessing import Pool
import contextlib
import time
import sys


def slow_sum( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then returns the sum of x and y"""
    time.sleep(nsecs)
    return x+y

def slow_diff( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then retruns the difference of x and y"""
    time.sleep(nsecs)
    return x-y

def broken_function( nsecs ):
    """Function that deliberately raises an AssertationError"""
    time.sleep(nsecs)
    raise ValueError("Called broken function")

if __name__ == "__main__":
    futures = []

    with contextlib.closing( Pool(processes=int(sys.argv[1])) ) as pool:
        futures.append( pool.apply_async( slow_sum, [3,6,7] ) )
        futures.append( pool.apply_async( slow_diff, [2,5,2] ) )
        futures.append( pool.apply_async( slow_sum, [1,8,1] ) )
        futures.append( pool.apply_async( slow_diff, [5,9,2] ) )
        futures.append( pool.apply_async( broken_function, [4] ) )

        while True:
            all_finished = True

            print("\nHave the workers finished?")

            for i in range(0,len(futures)):
                if futures[i].ready():
                    print("Process %d has finished" % i)
                else:
                    all_finished = False
                    print("Process %d is running..." % i)

            if all_finished:
                break

            time.sleep(1)

        print("\nHere are the results.")

        for i in range(0,len(futures)):
            if futures[i].successful():
                print("Process %d was successful. Result is %s" \
                   % (i, futures[i].get()))
            else:
                print("Process %d failed!" % i)

                try:
                    futures[i].get()
                except Exception as e:
                    print("Error = %s : %s" % (type(e), e))