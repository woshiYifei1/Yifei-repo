from typing import List

# O(n^2)
def reverse_pair_doubleLoop(alist):

    if (len(alist) < 2):
        return "The length of the list can not be less than 2"

    count = 0
    
    for i in range(0,len(alist)-1):
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                count += 1
    
    return count

# ------------------------------------------------------------------------------------
# O(n*log(n))
def reverse_pair_merge(nums:List[int]) -> int:

    if len(nums) < 2:
        return 0

    def merge_count(l, r):

        # separate the array til only one element left 
        if l >= r:
            return 0

        mid = (l+r)//2
        count = merge_count(l,mid) + merge_count(mid+1, r)

        temp[l:r+1] = nums[l:r+1]
        i, j = l, mid

        for k in range(l, r):
            if i == mid:
                nums[k] = temp[j]
                j += 1
            elif j == r or temp[j] >= temp[i]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
                count += mid - l

        return count


    temp = [0] * len(nums)
    return merge_count(0,len(nums))


ex_list = [4,3,2,1]
print(reverse_pair_merge(ex_list))
