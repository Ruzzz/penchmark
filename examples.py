from penchmark import benchmark_and_print, Callee, InData

def mul(x): return x[0] * x[1]
def nop(x): return x
callees = (mul, nop)
dataset = (
    InData(name='small-data', data=(2, 1), count_of_call=100000),
    InData(name='big-data', data=(200, 10), count_of_call=1000),
    InData(name='skipped-data', data=(1, 1), count_of_call=0)
)
benchmark_and_print(callees, dataset)
