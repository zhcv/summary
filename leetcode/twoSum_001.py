#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "HaipengZhang <zhp905@126.com>"

"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.
You may assume that each input would have exactly one solution, and you may not 
use the same element twice.


Example:
>> Given nums = [2, 7, 11, 15], target = 9,
>> Because nums[0] + nums[1] = 2 + 7 = 9,
>> return [0, 1].

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i
        return []

    def twoSum_1(self, nums, target):
        length_nums = len(nums)
        for i in range(length_nums):
            for j in range(i+1, length_nums):
                if nums[j] + nums[i] == target:
                   return i, j 
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 22
    f = Solution()
    print(f.twoSum_1(nums, target))
        
