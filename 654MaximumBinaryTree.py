class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if nums:
            maxinum = max(nums)
            maxindex = nums.index(maxinum)
            root = TreeNode(maxinum)
            root.left = self.constructMaximumBinaryTree(nums[:maxindex])
            root.right = self.constructMaximumBinaryTree(nums[maxindex+1:])
            return root 