from typing import List

# Problem 1
def list_sum_for_loop(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result += num
    return result

def list_sum_while_loop(nums: List[int]) -> int:
    result = 0
    idx = 0
    while idx < len(nums):
        result += nums[idx]
        idx += 1

    return result

def list_sum_recursion(nums: List[int], result = 0) -> int:
    if len(nums) == 0: 
        return result
    
    result += nums.pop()
    return list_sum_recursion(nums, result)
    

# Problem 2
def combine_list(s1: List[str], s2: List[str]) -> List[str]:
    # a, b, c  1,2
    n = min(len(s1), len(s2))
    i = 0 
    j = 0
    result = []
    while i < n or j < n:
        if i == j:
            result.append(s1[i])
            i += 1
        else:
            result.append(s2[j])
            j += 1
    while i < len(s1):
        result.append(s1[i])
        i += 1

    while j < len(s2):
        result.append(s2[j])
        j += 1
    
    return result
             

# Problem 3
def first_hundred_fibonacci(n = 100) -> List[int]:
    if n < 0:
        return []
    if n == 0: 
        return [0]
    if n == 1:
        return [0,1]
    
    prev_result = first_hundred_fibonacci(n-1)

    size = len(prev_result)
    cur_fib = prev_result[size-1] + prev_result[size-2]
    result = prev_result[:]
    result.append(cur_fib)

    return result

# Problem 4
def largest_formed_number(nums: List[int]) -> int:
    result = []
    for num in nums:
        temp = str(num)
        start_num = num
        if len(temp) > 1:
            start_num = int(temp[:1])
        
        res_size = len(result)
        for i, elem in enumerate(result):
            front_elem = int(str(elem)[:1])
            if start_num > front_elem:
                lhs = result[:i]
                lhs.append(int(temp))
                result = lhs + result[i:]
                break
        
        if len(result) == res_size:
            result.append(int(temp))
    
    str_result = ""
    for num in result:
        str_result += str(num)
        
    return int(str_result) if str_result else 0 

# Problem 5
def all_possible_expressions() -> List[str]:
    nums = "123456789"
    result = []

    def backtrack(index: int, expr: str) -> None:
        if index == len(nums):
            if eval(expr) == 100:
                result.append(expr)
            return
        
        ops = ["+", "-", ""] # possible operations are add, subtract and concatenate

        for op in ops:
            backtrack(index+1, expr + op + nums[index])
    
    backtrack(1, nums[0])
    return result


        