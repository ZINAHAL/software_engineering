#
# THIS CODE WAS TAKEN FROM: https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
#

# A recursive python program to find LCA of two nodes 
# n1 and n2 

# A Binary tree node 

class Node:
    # Constructor to create a new node
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


def get_data(root, given_key):
    if root is None:
        return None
    if given_key < root.key:
        return get_data(root.left, given_key)
    if given_key > root.key:
        return get_data(root.right, given_key)
    return root.data
    


# Function to find LCA of n1 and n2. The function assumes 
# that both n1(k1) and n2(k2) are present in BST 
def lca(root, k1, k2): 
	
	# Base Case 
	if (root is None) or (get_data(root, k1) is None) or (get_data(root, k2) is None): 
		return None

	# If both n1(k1) and n2(k2) are smaller than root, then LCA 
	# lies in left 
	if(root.key > k1 and root.key > k2): 
		return lca(root.left, k1, k2) 

	# If both n1(k1) and n2(k2) are greater than root, then LCA 
	# lies in right 
	if(root.key < k1 and root.key < k2): 
		return lca(root.right, k1, k2) 

	return root 

