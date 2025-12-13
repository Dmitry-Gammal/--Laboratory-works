import time, json, random


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")


def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)

        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)

        return result

    return wrapper


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

def f1(data):
    return sorted([x for x in Unique([job['job-name'] for job in data], ignore_case=True)], key=lambda x: x.lower())

def f2(data):
    return list(filter(lambda x: x.lower().startswith('программист'), data))

def f3(data):
    return list(map(lambda x: f"{x} с опытом Python", data))

@print_result
def f4(data):
    salaries = [random.randint(100000, 200000) for _ in data]
    return [f"{prof}, зарплата {salary} руб." for prof, salary in zip(data, salaries)]

if __name__ == '__main__':
    with open('data_light.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with cm_timer_1():
        f4(f3(f2(f1(data))))

