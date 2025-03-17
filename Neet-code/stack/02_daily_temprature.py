from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given a list of daily temperatures T, return a list such that, for each day in the input, 
        tells you how many days you would have to wait until a warmer temperature. 
        If there is no future day for which this is possible, put 0 instead.

        Args:
        temperatures (List[int]): List of daily temperatures

        Returns:
        List[int]: List of days until a warmer temperature
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack to store indices

        for i in range(n):
            # If the current temperature is higher than the previous one, 
            # calculate the difference of the indices and store the result
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
