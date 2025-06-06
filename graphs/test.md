# Two Sum

*Platform*: LeetCode | **Problem Number**: 1 | **Difficulty**: Easy  
*Category*: Arrays | **Pattern**: Two Pointer, Hash Map

## Problem Statement
[Original Problem Link](https://leetcode.com/problems/two-sum/)  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Approaches

### 1. Brute Force
- *Time Complexity*: O(n²)
- *Space Complexity*: O(1)
- *Description*: Use nested loops to check every pair of numbers in the array to find a pair that sums to the target.

### 2. Hash Map
- *Time Complexity*: O(n)
- *Space Complexity*: O(n)
- *Description*: Iterate through the array once, using a hash map to store numbers and their indices. For each number, check if its complement (`target - num`) exists in the hash map.

## Solution Code
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
