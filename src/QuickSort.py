def QuickSort(li=[]):
    if len(li) <= 1:
        return li
    else:
        return QuickSort([x for x in li if x < li[0]]) + \
               [x for x in li if x == li[0]] + \
               QuickSort([x for x in li if x > li[0]])


print QuickSort([5,6,9,0,78,99,23,8,4,9])