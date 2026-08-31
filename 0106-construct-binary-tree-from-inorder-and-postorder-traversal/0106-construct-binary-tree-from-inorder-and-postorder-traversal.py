class Solution:
    def buildTree(self, inorder, postorder):
        pos = {}

        for i in range(len(inorder)):
            pos[inorder[i]] = i

        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx

            if left > right:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.right = build(mid + 1, right)

            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)