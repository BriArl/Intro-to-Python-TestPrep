def in_order(nums):
    for i in range(len(nums) - 1):  # Loop through each index except the last one
        if nums[i] > nums[i + 1]:   # Compare current element with the next
            return False  # List is not sorted, return False immediately
    return True  # If loop completes, list is sorted
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')