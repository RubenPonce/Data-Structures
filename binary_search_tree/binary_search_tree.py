# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    node = self
   
    traversing_nodes = True
    while traversing_nodes:
      if value >= node.value and node.right:
        node = node.right

      elif value < node.value and node.left:
        node = node.left

      elif value >= node.value and not node.right:
        node.right = BinarySearchTree(value)
        traversing_nodes = False


      elif value < node.value and not node.left:
        node.left = BinarySearchTree(value)
        traversing_nodes = False

    

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    node = self
    
    traversing_nodes = True

    while traversing_nodes:

      if node.value is target:
        traversing_nodes = False
        return True
      #still traversing the binary search tree for target while nodes still exist
      elif target >=node.value and  node.right:
        node = node.right

      elif target <= node.value and node.left:
        node = node.left

      #found that the node doesnt contain the target
      elif target >= node.value and not node.right:
        traversing_nodes = False
        return False

      elif target <= node.value and not node.left:
        traversing_nodes = False
        return False


    pass

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    traversing_nodes = True
    node = self
    max = node.value
    while traversing_nodes:
      #still traversing the binary search tree for target while nodes still exist
      if node.right:
        node = node.right

      elif node.left:
        node = node.left

      elif node.value >= max:
        max = node.value
        traversing_nodes = False
      


    return max
      


    

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass