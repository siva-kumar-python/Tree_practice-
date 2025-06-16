class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.inorder()

    def count_nodes(self):
        left = self.left.count_nodes() if self.left else 0
        right = self.right.count_nodes() if self.right else 0
        return 1 + left + right

    def sum_of_nodes(self):
        left_sum = self.left.sum_of_nodes() if self.left else 0
        right_sum = self.right.sum_of_nodes() if self.right else 0
        return self.val + left_sum + right_sum

    def find_min(self):
        left_min = self.left.find_min() if self.left else self.val
        right_min = self.right.find_min() if self.right else self.val
        return min(self.val, left_min, right_min)

    def find_max(self):
        left_max = self.left.find_max() if self.left else self.val
        right_max = self.right.find_max() if self.right else self.val
        return max(self.val, left_max, right_max)
