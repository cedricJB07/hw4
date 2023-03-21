def merge(list1, list2):
    i = 0
    j = 0
    mergedList = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            mergedList.append(list1[i])
            i = i + 1
        else:
            mergedList.append(list1[i])
            j = j + 1
    mergedList.extend(list1[i:])
    mergedList.extend(list2[j:])
    return mergedList
