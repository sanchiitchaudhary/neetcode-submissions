class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        # Process remaining bars
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area