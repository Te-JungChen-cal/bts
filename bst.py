class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        # O(n)
        def helper(node):
            if node == None:
                return Node(value)
            if value < node.value:
                node.left = helper(node.left)
            else:
                node.right = helper(node.right)
            return node  
        helper(self)
        return self

    def search(self, value):
         # O(n)
        def helper(node):
            if node == None:
                return False
            if node.value == value:
                return True
            return helper(node.left) or helper(node.right)
       
        return helper(self)
        
    def min_value(self):
        def helper(node):
            if node == None:
                return -1
            if node.left == None:
                return node.value
            return helper(node.left)
        return helper(self)
    
    def max_value(self):
        def helper(node):
            if node == None:
                return -1
            if node.right == None:
                return node.value
            return helper(node.right)
        return helper(self)
    
    def in_order(self):
        def helper(node):
            if node == None:
                return 
            helper(node.left)
            print(node.data)
            helper(node.right)
        helper(self)

    def delete(self, value):
        def helper(node):
            if node == None:
                return None
            if node.value != value:
                if value < node.value:
                    node.left = helper(node.left)
                else:
                    node.right = helper(node.right)
            else:
                # no child
                if node.left == None and node.right == None:
                    return None
                # one child 
                elif node.right == None:
                    node.value = node.left.value
                    node.left = node.left.left
                    return node
                elif node.left == None:
                    node.value = node.right.value
                    node.right = node.right.right
                    return node
                # two child replace the value by the smallest in the right sub stree
                else:
                    temp_node = node.right
                    while temp_node.left != None and temp_node.left.left != None:
                        temp_node = temp_node.left
                        
                    if temp_node.left == None:
                        node.value = temp_node.value
                        node.right = temp_node.right
                    else:
                        node.value = temp_node.left.value
                        temp_node.left = None
            return node
                  
        return helper(self) 