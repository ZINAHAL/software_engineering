from lowestCommonAncestor import Node

root = None

#this function will be executed first before all the test functions
def setup_module():
    print("\nseting up the Binary Search Tree to test for LCA...")
    global root
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(4) 
    root.left.right = Node(12) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14)
    print("the tree is now complete...")



#this function will be executed last after all the test functions are completed
def teardown_module():
    print("\nall the tests are done")