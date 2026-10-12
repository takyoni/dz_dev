class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:  # уже встречали нужное число
                return [seen[need], i]
            seen[num] = i  # запоминаем число и его индекс
