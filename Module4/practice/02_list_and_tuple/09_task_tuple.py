# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# Да отрубят мне руки за такой код, но как умею..

import random

tup1 = tuple([random.randint(1, 15) for _ in range(random.randint(1, 10))])
tup2 = tuple([random.randint(1, 15) for _ in range(random.randint(1, 10))])
tup3 = tuple([random.randint(1, 15) for _ in range(random.randint(1, 10))])

print(*tup1, "\n", *tup2, "\n", *tup3)

minimal_tuple = []
min_tuple_lens = min(len(tup1), len(tup2), len(tup3))

count = 0

if len(tup1) == min_tuple_lens:
    minimal_tuple.extend(tup1)
elif len(tup2) == min_tuple_lens:
    minimal_tuple.extend(tup2)
else:
    minimal_tuple.extend(tup3)

for number in minimal_tuple:
    if number in tup1 and number in tup2 and number in tup3:
        count += 1

print(min_tuple_lens, *minimal_tuple, count)
