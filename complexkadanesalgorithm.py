nums = [-2,1,-3,4,-1,2,1,-5,4]
def max_subarray_sum_with_subarray(nums):
    max_sum =float('inf')
    current_sum = 0
    start = end =0
    temp_start =0
    for i ,num in enumerate(nums):
        if num > current_sum +num:
            current_sum =num
            temp_start =i
        else:
            current_sum +=num
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_startend = i
    return max_sum,nums[start:end+1]
max_sum,subarray=max_subarray_sum_with_subarray(nums)
print("Max Sum:",max_sum)
print("Subarray:",subarray)