def merge_sort(arr):
    if len(arr) > 1:
        # how can we get the middle of the array ?
        mid = len(arr) // 2 
        # divide into two halves  : //subarrays
        left_half = arr[:mid]
        right_half = arr[mid:]
        # recursive sort 
        merge_sort(left_half)
        merge_sort(right_half)

        # logic arrangement for my subarrays 
        # merge the two sorted halves 
        i = 0 
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1 
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # 7 two halves 3,3 -> 1
        # check for any remaining elements in the left and right halves 
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1 
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1 
            k += 1

#  example usage 
if __name__ == "__main__":
    arr  = [12,11,13,5,6,7,15]
    print("Unsorted array " , arr)


    merge_sort(arr)
    print("sorted array ", arr)
