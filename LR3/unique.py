import random

def gen_random(count, min, max):
    for i in range(count):
        yield random.randint(min, max)


class Unique(object):

    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self._setup_next_value()

    def _setup_next_value(self):
        self.next_value = None
        self.next_ready = False

        for item in self.items:
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                self.next_value = item
                self.next_ready = True
                break

    def __next__(self):
        if not self.next_ready:
            raise StopIteration

        result = self.next_value
        self._setup_next_value()
        return result

    def __iter__(self):
        return self

test1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
test2 = gen_random(10, 1, 3)
test3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

for i in Unique(test1):
    print(i, end=' ')
print()
for i in Unique(test2):
    print(i, end=' ')
print()
for i in Unique(test3, ignore_case=True):
    print(i, end=' ')