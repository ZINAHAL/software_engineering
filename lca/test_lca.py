from lowestCommonAncestor import Node, lca, get_data

root = None

#this function will be executed first before all the test functions
def setup_module():
    global root
    root = Node(20, 'a') 
    root.left = Node(8, 'b') 
    root.right = Node(22, 'c') 
    root.left.left = Node(4, 'd') 
    root.left.right = Node(12, 'e') 
    root.left.right.left = Node(10, 'f') 
    root.left.right.right = Node(14, 'g')


def test_when_given_nodes_are_present():
    global root
    assert lca(root, 10, 14).key == 12
    assert lca(root, 4, 14).key == 8
    assert lca(root, 22, 14).key == 20
    assert lca(root, 4, 22).key == 20
    assert lca(root, 20, 20).key == 20
    assert lca(root, 14, 14).key == 14
    assert lca(root, 20, 14).key == 20
    assert lca(root, 14, 8).key == 8


def test_when_some_given_nodes_are_present():
    assert lca(root, 999, 14) == None
    assert lca(root, 8, 999) == None
    assert lca(root, 999, 20) == None
    

#this function will be executed last after all the test functions are completed
def teardown_module():
    print("\nall the tests are done")