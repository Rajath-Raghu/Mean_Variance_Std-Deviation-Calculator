from itertools import islice


def convert(list2, len_3d):
   res = iter(list2)
   return [list(islice(res, i)) for i in len_3d]