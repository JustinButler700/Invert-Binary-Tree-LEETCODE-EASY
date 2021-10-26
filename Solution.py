#Justin Butler 10/25/2021
class Solution(object):
    def invertTree(self, root):
        if root is None: return None
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root
        
