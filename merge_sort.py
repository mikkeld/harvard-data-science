import sys
import math

'''
Uses Merge sort to sort list of n integers
'''


def merge_sort(list, left_right):
    print(str(list) + " " + left_right)
    if len(list) < 2:
        return list

    half = len(list) // 2

    list1 = merge_sort(list[:half], "left")
    list2 = merge_sort(list[half:], "right")

    return merge(list1, list2)


def merge(list1, list2):
    print("Merge called")
    merged = []

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            merged.append(list2[0])
            del list2[0]
        else:
            merged.append(list1[0])
            del list1[0]

    while len(list1) > 0:
        merged.append(list1[0])
        del list1[0]

    while len(list2) > 0:
        merged.append(list2[0])
        del list2[0]

    print("result of merged: " + str(merged))
    return merged


print(merge_sort([4, 2, 6, 8, 7, 5, 3, 6], ""))
