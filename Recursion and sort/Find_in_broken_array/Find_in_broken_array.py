# 59225370
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1

    mid = find_pivot(nums, left, right)
    if mid == -1:
        mid = (left + right) // 2
    left = 0
    right = len(nums) - 1
    while left <= right:
        if target == nums[mid]:
            return mid
        if target < nums[mid] and target >= nums[left]:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
    return -1


def find_pivot(arr, low, high):
    if high < low:
        return -1
    elif high == low:
        return low
    mid = (low + high) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)
