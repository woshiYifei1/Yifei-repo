import time

def merge_sort(list):

    #如果list长度小于等于1，那就不排序
    if (len(list) <= 1):
        return list     #赋值left和right
    
    #找到list的中间点
    mid = int(len(list)/2)

    #把每一个list分裂成两个，直到通过第一个条件语句之后给left和right赋值
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    #当left和right的长度都为1时，开始逐渐合并小list然后重新赋值给left和right
    return merge(left, right)


#逐渐合并小list成一个完整的大list
def merge(list1, list2):

    ordered_list = []
    i = 0  
    j = 0

    #用两个坐标，i和j，来排序lists里面的数字，从小到大
    while (i < len(list1) and j < len(list2)):
        if (list1[i] < list2[j]):
            ordered_list.append(list1[i])
            i += 1
        else:
            ordered_list.append(list2[j])
            j += 1
    
    #在list都被sorted的情况下，没被加完的list可以把剩下的元素直接合并进ordered_list
    if (i >= len(list1)):
        ordered_list += list2[j:len(list2)]
    if (j >= len(list2)):
        ordered_list += list1[i:len(list1)]
        
    
    return ordered_list


#对整个过程计算时间
start_time = time.time()

example_list = [11,99,33,69,77,88,55,11,33,36,39,66,44,22]
result = merge_sort(example_list)
print(result)

end_time = time.time()

print("total usage of time is %f sec" %(end_time - start_time))