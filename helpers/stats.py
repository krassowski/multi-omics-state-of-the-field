import random
from typing import Iterable, Callable


def bootstrap(data: Iterable, stat: Callable, ci=.95, r=1000):
    if not isinstance(data, list):
        data = list(data)
    distribution = sorted([
        stat(random.choices(data, k=len(data)))
        for i in range(r)
    ])
    return {
        'lower': distribution[int((1 - ci) * r)],
        'upper': distribution[int(ci * r)]
    }
