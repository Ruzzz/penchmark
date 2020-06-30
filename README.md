# Python code benchmark library

## Examples

```python
from penchmark import benchmark_and_print, Callee, InData

callees = (
    Callee(callee_name='mul', callee=lambda x: x[0] * x[1]),
    Callee(callee_name='nop', callee=lambda x: x)
)
dataset = (
    InData(name='small-data', data=(2, 1), count_of_call=100000),
    InData(name='big-data', data=(200, 10), count_of_call=1000),
    InData(name='skipped-data', data=(1, 1), count_of_call=0)
)
benchmark_and_print(callees, dataset)
```

or

```python
from penchmark import benchmark_and_print

callees = (
    ('mul', lambda x: x[0] * x[1]),
    ('nop', lambda x: x)
)
dataset = (
    ('small-data', (2, 1), 100000),
    ('big-data', (200, 10), 1000),
    ('skipped-data', (1, 1), 0)
)
benchmark_and_print(callees, dataset)
```

### Result

#### small-data

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| nop           |    0.0049 |  1.0000 |
| mul           |    0.0077 |  1.5886 |

#### big-data

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| nop           |    0.0000 |  1.0000 |
| mul           |    0.0001 |  1.7242 |

#### Summary

| callee_name   |   mean |   median |
|:--------------|-------:|---------:|
| nop           | 1.0000 |   1.0000 |
| mul           | 1.6564 |   1.6564 |

```python
from penchmark import benchmark_and_print

def mul(x): return x[0] * x[1]
def nop(x): return x

dataset = (
    ('small-data', (2, 1), 100000),
    ('big-data', (200, 10), 1000),
    ('skipped-data', (1, 1), 0)
)
benchmark_and_print((mul, nop), dataset)
```

### Result

#### small-data

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| __main__.nop  |    0.0049 |  1.0000 |
| __main__.mul  |    0.0079 |  1.6041 |

#### big-data

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| __main__.nop  |    0.0000 |  1.0000 |
| __main__.mul  |    0.0001 |  1.7752 |

#### Summary

| callee_name   |   mean |   median |
|:--------------|-------:|---------:|
| __main__.nop  | 1.0000 |   1.0000 |
| __main__.mul  | 1.6896 |   1.6896 |
