import random


def gen_random(count, min, max):
    for i in range(count):
        yield random.randint(min, max)


result = gen_random(5, 1, 3)
for i in result:
    print(i, end=' ')
