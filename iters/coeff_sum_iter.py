"""
coeff_sum_iter
"""
from synth.decorators import length

@length(lambda *args: max([len(iter) for (k,iter) in args]))
def coeff_sum_iter(*args):
    """
    Return the sum of the yielded numbers from each of the input iterators.
    """
    work = [(k,iter,()) for (k,iter) in args]
    while len(work) != 0:
        n = None
        for i,(k,iter,res) in enumerate(work):
            if len(res) == 0:
                try:
                    res = iter.next()
                except StopIteration:
                    del work[i]
                    continue
                else:
                    work[i] = (k,iter,res)
            if n is None:
                n = len(res)
            else:
                n = min(n,len(res))
        if n is not None:
            yi = [0] * n
            for i,(k,iter,res) in enumerate(work):
                yi = [yi[j] + k*res[j] for j in xrange(n)]
                work[i] = (k,iter,res[n:])
            yield [int(x+0.5) for x in yi]
