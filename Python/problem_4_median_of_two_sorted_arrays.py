class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if not len(nums1) and not len(nums2):
            return
        arr = nums1 + nums2
        self.sort_arr(arr)
        return self.median(arr)

    def sort_arr(self, arr):
        for i in range(len(arr)):
            j = i
            anchor = arr[i]
            while j > 0 and anchor < arr[j-1]:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = anchor

    def median(self, sorted_arr):
        n = len(sorted_arr)
        if n == 1:
            return sorted_arr[0]
        if n % 2 == 0:
            return (sorted_arr[n//2-1] + sorted_arr[(n)//2])/2
        return sorted_arr[(n)//2]


# driver code
test_cases = [[[1, 3], [2]], [[5, 2, 7], [4, 2, 1]], [[], [1]], [[], []]]
sol = Solution()

for test in test_cases:
    print(sol.findMedianSortedArrays(test[0], test[1]))
