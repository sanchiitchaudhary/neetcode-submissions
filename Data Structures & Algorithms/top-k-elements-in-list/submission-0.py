class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency
        arr = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Take top k elements
        result = []

        for i in range(k):
            result.append(arr[i][0])

        return result