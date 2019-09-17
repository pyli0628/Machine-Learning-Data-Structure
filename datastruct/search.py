# 二分查找 O(logn)
def binary_search(lis,key):
    left = 0
    right = len(lis)-1
    while left<right:
        mid = int((left+right)/2)
        if key < lis[mid]:
            right = mid-1
        elif key > lis[mid]:
            left = mid+1
        else:
            return mid
    return False
# 斐波那契数列分割（加法分割） O(logn)

