def quick_sort(arr):
    if len(arr) < 2:
        return arr
    provo = arr[0]
    smaill_arr = [i for i in arr[1:] if i < provo]
    big_arr = [i for i in arr[1:] if i >= provo]
    return quick_sort(smaill_arr) + [provo] + quick_sort(big_arr)


print(quick_sort([6, 2, 0, -1. - 3, 100, 29]))