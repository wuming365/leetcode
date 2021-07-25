from typing import List
from icecream import ic


def twoSum1(nums: List[int], target: List[int]):
    """空间复杂度O(n)，时间复杂度O(n)

    Args:
        nums (List[int]): [description]
        target (List[int]): [description]

    Returns:
        [type]: [description]
    """
    hashtable = {}  #由于函数要进出栈操作，因此dict()比{}慢
    for i, num in enumerate(nums):
        difference = target - num
        if difference in hashtable:  #多次使用target-num，可把其提取为变量，可减少运行用时
            return [i, hashtable[difference]]
        hashtable[num] = i  #放在if语句后可保证相同索引的值相加为target
    return []


def twoSum2(nums: List[int], target: List[int]):
    """空间复杂度O(1)，时间复杂度O(n2)

    Args:
        nums (List[int]): [description]
        target (List[int]): [description]

    Returns:
        [type]: [description]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def main():
    a = [2, 4, 6]
    ic(twoSum1(a, 8))
    ic(twoSum2(a, 8))


if __name__ == "__main__":
    main()
