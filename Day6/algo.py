def Linear_Search(target, data):#n
    for i in range(len(data)):
        if data[i] == target:
            return i
    return None

def Binary_Search(target, data):#lgn
    #資料必須要排序過
    upper, lower = len(data)-1, 0
    while upper > lower:
        mid = (upper+lower)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            upper = mid-1
        else:
            lower = mid+1
    return None

l = [1,2,3,4,5,6]
print(Binary_Search(13, l))
