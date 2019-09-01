# -*- coding: utf-8 -*-
from functools import reduce
arr_msg = [x for x in range(11)]
arr_msg = list(map(str, arr_msg))

fin_msg = "XXX: "
print(list(range(1, len(arr_msg), 2)))
print(reduce(lambda x, y: x + arr_msg[y] + " " + arr_msg[y + 1] + " ", range(1, len(arr_msg), 2), fin_msg))
