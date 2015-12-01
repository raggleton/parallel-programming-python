from multiprocessing import Pool, current_process
import contextlib
import time

def sum( (x, y) ):
    """Return the sum of the arguments"""
    print("Worker %s is processing sum(%d,%d)" \
             % (current_process().pid, x, y) )
    time.sleep(1)
    return x+y

def product( (x, y) ):
    """Return the product of the arguments"""
    print("Worker %s is processing product(%d,%d)" \
             % (current_process().pid, x, y) )
    time.sleep(1)
    return x*y

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    work = zip(a,b)

    # Now create a Pool of workers
    with contextlib.closing( Pool(processes=4) ) as pool:
        sum_future = pool.map_async( sum, work, chunksize=3 )
        product_future = pool.map_async( product, work, chunksize=3 )

        sum_future.wait()
        product_future.wait()

    total_sum = reduce( lambda x,y: x+y, sum_future.get() )
    total_product = reduce( lambda x,y: x+y, product_future.get() )

    print("Sum of sums of 'a' and 'b' is %d" % total_sum)
    print("Sum of products of 'a' and 'b' is %d" % total_product)