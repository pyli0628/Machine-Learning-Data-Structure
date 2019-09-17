
#直接插入排序 时间O(n^2) 空间O(1) 稳定
def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i]<array[j]:
                array.insert(j,array.pop(i))
                break
    return array

#快速排序 时间O(nlog₂n) 空间O(nlog₂n) 不稳定
def quick_sort(array):

    def recur(begin,end):
        # begin & end is index
        if begin>end:
            return
        l,r = begin,end
        base = array[l]
        while l<r:
            while l<r and array[r]>base:
                r-=1
            array[l]=array[r]
            while l<r and array[l]<=base:
                l+=1
            array[r] = array[l]
        array[r]=base

        recur(begin,l-1)
        recur(r+1,end)
    recur(0,len(array)-1)
    return array

# 冒泡排序 O(N^2) O(1)  稳定
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    return array

# 选择排序 O(n^2)  O(1) 不稳定
def select_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i,len(array)):
            if array[j]<array[x]:
                x = j
        array[i],array[x] = array[x],array[i]
    return array

# 归并排序 O(nlog2n) O(n) 稳定
def merge_sort(array):
    def merge(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0]<=arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0]>arr_r[0]:
                array.append((arr_r.pop(0)))
        if len(arr_l)>0:
            array+=arr_l
        elif len(arr_r)>0:
            array+=arr_r
        return array
    def recur(array):
        if len(array)==1:
            return array
        mid = len(array)//2
        arr_l = recur(array[:mid])
        arr_r = recur(array[mid:])
        return merge(arr_l,arr_r)
    return recur(array)

#堆排序 O(nlog2n) O(1) 不稳定


if __name__ == '__main__':
    lst = [3,4,2,5,1,6,9,1,3]
    # lst.sort()
    # print(lst)
    # print(sorted(lst))
    #print(insert_sort(lst))
    #print(quick_sort(lst))
    print(lst)
    print(select_sort(lst))
    print(merge_sort(lst))
    # print(bubble_sort(lst))