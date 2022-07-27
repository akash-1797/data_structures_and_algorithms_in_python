class Node:
  def __init__(self,data):
    self.data = data
    self.next = None



def take_input():
  input_list = [int(x) for x in input().split()]
  head = None
  for curr_data in input_list:
    if curr_data == -1:
      break
    new_node = Node(curr_data)
    if head == None:
      head = new_node
      tail = new_node
    else:
      tail.next = new_node
      tail = new_node
  return head

def print_ll(head):
  curr  = head
  while (curr != None):
    print(str(curr.data) + '-->',end=' ')
    curr = curr.next
  print('None')


def lenght_of_ll(head):
  curr = head
  count = 0
  while(curr != None):
    count = count + 1
    curr = curr.next
  return count

def print_ith_node(head,i):
  count = 0
  curr = head
  while(curr != None):
    if count == i:
      return curr.data
    curr = curr.next
    count  = count + 1

def insertion_at_ith_position(head,i,data):
  if i < 0 or i > lenght_of_ll(head):
    return head
  count = 0
  prev = None
  curr = head
  while(count < i):
    prev = curr
    curr = curr.next
    count = count + 1
  new_node = Node(data)
  if prev == None:
    head = new_node
  else:
    prev.next = new_node
  new_node.next = curr
  return head


def delete_node_from_ith_position(head,pos):
  if head == None:
    return head
  if pos == 0 :
    head = head.next
    return head
  count = 0
  prev = None
  curr = head
  while(count < i ):
    prev = curr
    curr = curr.next
    count = count + 1
  if curr != None:
    temp = curr.next
  if count == lenght_of_ll(head):
    return head
  prev.next = temp
  return head
    
def lenght_of_ll_recursivly(head):
  if head == None:
    return 0
  small = 1 + lenght_of_ll_recursivly(head.next)
  return small

def insertion_recursively_at_ith_position(head,pos,data):
  if pos < 0:
    return head
  if pos == 0:
    new_node = Node(data)
    new_node.next = head
    return new_node
  if head == None:
    return head
  smallhead = insertion_recursively_at_ith_position(head.next,pos-1,data)
  head.next = smallhead
  return head
  
def deletion_at_ith_pos(head,pos):
  if pos < 0:
    return head
  if head == None:
    return head
  if pos == 0:
    temp = head.next
    return temp
  small_head = deletion_at_ith_pos(head.next,pos-1)
  head.next = small_head
  return head

def linear_search_in_ll(head,n):
  if head == None:
    return
  count  = 0
  curr = head
  while(curr != None):
    if curr.data == n:
      return count
    curr = curr.next
    count = count +1
  return -1


def append_to_last(head,n):
  if head == None:
    return None
  if n == 0:
    return head
  x = lenght_of_ll(head) - n
  t1 = head
  t2 = head
  count= 0
  while(count < x -1):
    t1 = t1.next
    count = count+1
  head = t1.next
  t1.next = None
  tail = head 
  while(tail.next != None):
    tail = tail.next
  tail.next = t2
  return head
  
def remove_duplicates(head):
  if head == None:
    return head
  p = head
  while(p != None and p.next != None):
    if p.data == p.next.data:
      q = p.next.next
      if q == None:
        p.next = None
        break
        return head
      p.next = q
    if p.data != p.next.data:
      p = p.next
  return head
  
    
  
head = take_input()
head = remove_duplicates(head)
print_ll(head)
