#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a 
specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated 
description carefully.
"""
# =====================================================================================

class Solution(object):
    def twoSum(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        value2index = {}
        for i, num in enumerate(nums):
            if target - num in value2index:
                return [value2index[target - num], i]
            else:
                value2index[num] = i
        return []


if __name__ == '__main__':
    nums = [2,3,5,7,9]
    target = 10
    solu = Solution()
    result = solu.twoSum(nums, target)
    print result

