def calc_average(nums):
    if not nums:  # Handle empty list case
        return 0.0
    
    total_sum = sum(nums)  # Calculate sum of all elements in nums
    average = total_sum / len(nums)  # Compute average as sum divided by number of elements
    return average
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0