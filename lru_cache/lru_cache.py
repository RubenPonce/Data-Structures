import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.storage = {}
    self.node_count = 0
    self.linked_list = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  
  def get(self, key):


    if key not in self.storage or self.node_count is 0:
      return None
    else:
      node = self.storage[key]
      self.linked_list.delete(node[1])
      self.linked_list.add_to_head([key, node[0]])
      self.node_count += 1
      return node[0]
      

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    
    if self.limit is self.node_count:
      #remove old node
      self.linked_list.remove_from_tail()
      del self.storage[self.linked_list.tail.value[0]]
      self.node_count -= 1
    if key in self.storage:
      #node_count stays the same because nothing was deleted
      self.linked_list.delete(self.storage[key][1])
      self.linked_list.add_to_head([key, value])
      self.storage[key] = [value, self.linked_list.head]
      
      return
      

    
    #instead of updating just add it to the head
    self.linked_list.add_to_head([key, value])
    self.storage[key] = [value, self.linked_list.head]
    self.node_count += 1


