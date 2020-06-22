# 给定一个二叉树，它的每个结点都存放着一个整数值。 
# 
#  找出路径和等于给定数值的路径总数。 
# 
#  路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。 
# 
#  示例： 
# 
#  root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
#  
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        s=[]
        ans=0
        def dfs(node):
            nonlocal s
            nonlocal ans
            if node==None:
                return
            else:
                for i,x in enumerate(s):
                    # if node.val==sum-x:
                    #     ans+=1
                    s[i]=x+node.val
                s.append(node.val)
                for x in s:
                    if x==sum:
                        ans+=1
                dfs(node.left)
                dfs(node.right)
                del s[-1]
                for i,x in enumerate(s):
                    s[i]=x-node.val
        dfs(root)
        return ans



        
# leetcode submit region end(Prohibit modification and deletion)
