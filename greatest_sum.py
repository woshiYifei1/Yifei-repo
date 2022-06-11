import time

def find_greatest_sum(list):

    if (len(list) == 0):
        return -1
    elif (len(list) == 1):
        return list[0]

    sum = 0
    greatest_sum = 0
    
    for i in range(0,len(list)):
        sum += list[i]

        if (sum < 0):
            sum = 0
        
        greatest_sum = max(greatest_sum, sum)
    
    return greatest_sum

if __name__ == '__main__':
    start_time = time.time()

    ex_list = [-1,-3,3,5,-4,3,2,-2,3,6]
    print(find_greatest_sum(ex_list))

    end_time = time.time()

    print("total usage of time is %f sec" %(end_time - start_time))
