def sum_arr(arr):
    sum = 0
    for item in arr:
        sum  += item
    return sum 

def largest_elm(arr):
    max = arr[0]
    for item in arr:
        if max < item:
            max = item
    return max

def arr_rotat(arr, n):
    tmp_arr = []
    for item in range(0,n):
        tmp = arr[0]
        for item in range(1, len(arr)):
            arr[item-1] = arr[item]
        arr[-1] = tmp
    return arr    

def split_merg(arr, n):
    tmp_arr = arr[0:n]
    arr[:] = arr[n:] + tmp_arr
    return arr   

def mul_rem(arr, n):
    tmp_arr = arr
    for item in arr:
        tmp_arr[item] = item%n
    mul_prd = tmp_arr[0]
    for item in range(1,len(tmp_arr)-1):
        mul_prd *= tmp_arr[item]
    return mul_prd%n

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    sum = sum_arr(arr)
    max = largest_elm(arr)
    # rotat_arr = arr_rotat(arr, 1)
    # sp_mg = split_merg(arr, 2)\
    rem = mul_rem(arr, 8)
    print(f'Sum - {sum}')
    print(f'Max - {max}')
    # print(f'Rotated Arr - {rotat_arr}')
    # print(f'Split/Merger Arr - {sp_mg}')
    print(f'Reminder - {rem}')