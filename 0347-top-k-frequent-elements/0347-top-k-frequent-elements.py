from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        return heapq.nlargest(k, Counter(nums).keys(), key=Counter(nums).get)
        