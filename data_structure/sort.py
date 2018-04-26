__author__ = 'dharmesh'


def _swap(A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp


def bubble_sort(li):
    loop = 0
    for i in range(len(li)):
        for j in range(i + 1,len(li)):
            if li[i] > li[j]:
                _swap(li,i,j)
            loop += 1
            print loop
    return li


def selection_sort(li):
    loop = 0
    for i in range(len(li)):
        mini = i
        for j in range(i + 1,len(li)):
            if li[mini] > li[j]:
                mini = j
            loop += 1
            print loop
        _swap(li,mini,i)
    return li


def insertion_sort(li):
    loop = 0
    for i in range(1,len(li)):
        val = li[i]
        divider = i
        for j in range(divider, 0, -1):
            if li[j - 1] > val:
                _swap(li, j - 1, j)
                loop += 1
                print loop
    return li


def rotate_elements(n, A):
    temp_li = A[-n:]
    for i in range(len(A) - 1, n - 1, -1):
        A[i] = A[i - n]
    for j in range(len(temp_li)):
        A[j] = temp_li[j]
    return A


def sort_by_length():
    li = ['abdjvndjf', 'adsfa', 'sdkfjgdfkk', 'asdff']
    len_dict = {}
    for word in li:
        key = len(word)
        if key in len_dict:
            [len_dict[key]]
        len_dict[len(word)] = word
    print len_dict


def merge_sort(l):

    n = len(l)
    if n <= 1:
        return l  # return list if length is 1

    #  dividing the list in two equal parts
    div = n // 2
    left_half = l[:div]
    right_half = l[div:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    #  merging two sorted lists
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        # if merged element of left is small merge it else right
        if left_half[i] <= right_half[j]:
            l[k] = left_half[i]
            i += 1
            k += 1
        else:
            l[k] = right_half[j]
            j += 1
            k += 1
    while i < len(left_half):
        l[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        l[k] = right_half[j]
        j += 1
        k += 1
    print 1
    return l


def quick_sort(A, start, end):
    pivot = end
    pindex = start
    print A
    if end - start < 1:
        return A
    for i in range(start, end):
        if A[i] < A[pivot]:
            _swap(A,i,pindex)
            pindex += 1
    _swap(A, pindex, pivot)
    # print A
    quick_sort(A, start, pindex - 1)
    # print A1
    quick_sort(A, pindex + 1, end)
    # print A2
    return A


def find_dupilcate(st):
    for s in st:
        for s in st:
            pass
