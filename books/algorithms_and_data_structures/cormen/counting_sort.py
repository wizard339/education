def counting_sort(arr):
    k = max(arr)
    # creating an array to store the number of elements
    counts_arr = [0] * (k + 1)
    # creating an array to store the sorted sequence
    result_arr = [0] * len(arr)
    
    for j in range(len(arr)):
        counts_arr[arr[j]] += 1
    # now counts_arr[j] contains the number of elements equal to j

    for i in range(1, k + 1):
        counts_arr[i] += counts_arr[i - 1]
    # now counts_arr[i] contains the number of elements not exceeding i
    
    for j in range(len(arr) - 1, -1, -1):
        result_arr[counts_arr[arr[j]] - 1] = arr[j]
        counts_arr[arr[j]] -= 1
        
    return result_arr

if __name__ == '__main__':
    a = [4, 8, 3, 1, 5, 5]
    print(counting_sort(a))
