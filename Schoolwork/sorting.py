from re import A, purge


l = [46, 53, 7, 70, 36, 35, 14, 2, 29, 5, 98, 60]

def quicksort(listIn):
        if len(listIn) > 1:
                pivot = listIn[-1]
                belowPiv = []
                for item in listIn[:-1]:
                        if item < pivot:
                                belowPiv.append(item)
                abovePiv = []
                for item in listIn[:-1]:
                        if item > pivot:
                                abovePiv.append(item)
                return quicksort(belowPiv) + [pivot] + quicksort(abovePiv)
        else:
                return listIn


def quicksortReverse(listIn):
        if len(listIn) > 1:
                pivot = listIn[-1]
                belowPiv = []
                for item in listIn[:-1]:
                        if item < pivot:
                                belowPiv.append(item)
                abovePiv = []
                for item in listIn[:-1]:
                        if item > pivot:
                                abovePiv.append(item)
                return quicksortReverse(abovePiv) + [pivot] + quicksortReverse(belowPiv)
        else:
                return listIn


def quicksortReverse2(listIn):
        if len(listIn) > 1:
                pivot = listIn[-1]
                belowPiv = []
                for item in listIn[:-1]:
                        if item > pivot:
                                belowPiv.append(item)
                abovePiv = []
                for item in listIn[:-1]:
                        if item < pivot:
                                abovePiv.append(item)
                return quicksortReverse2(belowPiv) + [pivot] + quicksortReverse2(abovePiv)
        else:
                return listIn

def quicksortReverseDirty(listIn):
	sortedList = quicksort(listIn)
	return list(reversed(sortedList))


print(f"Unsorted: {l}")
print(f"Quicksort: {quicksort(l)}")
print(f"Quicksort Reverse: {quicksortReverse(l)}")
# print(f"Quicksort Reverse 2: {quicksortReverse2(l)}")
# print(f"Quicksort Reverse Dirty Solution: {quicksortReverseDirty(l)}")