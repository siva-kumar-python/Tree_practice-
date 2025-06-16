from tree_node import TreeNode

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:")
root.inorder()
print("\nCount of nodes:", root.count_nodes())
print("Sum of nodes:", root.sum_of_nodes())
print("Min:", root.find_min())
print("Max:", root.find_max())
