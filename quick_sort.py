from typing import List


def quick_sort(alist : List[int]):

    # core of quick sort - let smaller goes in front of the pivot and greater goes behind
    def partition_sort(alist, left, right):

        j = left
        # set the pivot point to be the rightmost element
        pivot = right
    
        # compare the every element with the pivot element and swap the smaller to the front
        for i in range(left, right):
            if alist[i] <= alist[pivot]: 
                alist[i], alist[j] = alist[j], alist[i]
                j += 1
        
        # swap the pivot to the middle
        alist[j], alist[pivot] = alist[pivot], alist[j]
        
        # return the index of the pivot
        return j
    
    # split the list and sort them using the function 'partition_sort'
    def split_n_sort(alist, left, right):

        # split the list in three part: the smaller numbers, pivot, and the greater numbers 
        # split until the length is 1
        if left < right:
            pivot = partition_sort(alist, left, right)
            split_n_sort(alist, left, pivot-1)
            split_n_sort(alist, pivot+1, right)

    split_n_sort(alist, 0, len(alist)-1)

    return alist

ex_list = [10, 7, 8, 9, 1, 5]
print(quick_sort(ex_list))