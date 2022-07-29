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

def reverse_linked_list_iteraretively(head):
  if head == None and head.next == None:
    return head
  curr = head
  prev = None
  while(curr != None):
    temp = curr.next
    curr.next = prev
    prev = curr
    curr =temp
  return prev
    
  
def reverse_linked_list_recursively(head):
  if head == None or head.next == None:
    return head
  new_head = reverse_linked_list_recursively(head.next)
  head_next = head.next
  head_next.next = head
  head.next = None
  return new_head



def merge_sorted_linked_list(head1,head2):
  curr = dummy = Node(0)
  while(head1 and head2):
    if head1.data <= head2.data:
      dummy.next = head1
      head1 = head1.next
    else:
      dummy.next = head2
      head2 = head2.next
    dummy = dummy.next
  if head1 == None:
    dummy.next =  head2
  if head2 == None:
    dummy.next = head1
  return curr.next


def mid_point(head):
  if head == None or head.next == None:
    return head
  fast = head
  slow = head
  while(fast.next and fast.next.next):
    fast = fast.next.next
    slow = slow.next
  return slow

def merge_sort_on_ll(head):
  if head == None or head.next == None:
    return head
  middle = mid_point(head)
  next_to_middle  = middle.next
  middle.next = None
  l1 = merge_sort_on_ll(head)
  l2 = merge_sort_on_ll(next_to_middle)
  new_head = merge_sorted_linked_list(l1,l2)
  return new_head

def evenAfterOdd(head):
  odd_head = None
  odd_tail = None
  even_head = None
  even_tail = None
  if head == None:
    return head
  curr = head
  while(curr):
    if curr.data % 2 != 0:
      if odd_head is None:
        odd_head = curr
        odd_tail = curr
      else:
        odd_tail.next = curr
        odd_tail = curr
    else:
      if even_head == None:
        even_head = curr
        even_tail= curr
      else:
        even_tail.next = curr
        even_tail = curr
    curr = curr.next
        
  if odd_head != None and odd_tail != None and even_head != None and even_tail != None:
    odd_tail.next = None
    even_tail.next = None
    odd_tail.next = even_head
    return odd_head
  if odd_head == None:
    return even_head
  else:
    return odd_head



def delete_n_nodes(head,M,N):
  if head == None and M ==0 :
    return None
  if N == 0:
    return head
  curr = head
  while(curr != None):
    for i in range(1,M):
      if curr != None:
        curr = curr.next 
    t = curr.next
    for i in range(1,N+1):
      if t == None:
        break
      t= t.next
    if curr != None:
      curr.next = t
    curr = t
  return head

def swap_nodes_at_ith_and_jth(head,i,j):
  if  i== j:
    return head
  if j<i:
    i,j = j,i
  previ = None
  curri = head
  for k in range(i):
    previ = curri
    curri = curri.next
  prevj = previ
  currj = curri
  for k in range(i,j):
    prevj = currj
    currj = currj.next
  if previ == None:
    currj = head
  else:
    previ.next = currj
  if prevj == None:
    curri = head
  else:
    prevj.next = curri
    prevj.next = curri
  temp = currj.next
  currj.next = curri.next
  curri.next = temp 
  return head



def kReverse(head, k):
  if head == None:
    return None
  if k == 0:
    return head
  curr = head
  prev = None
  count = 0 
  while(curr != None and count < k):
    count = count + 1
    next = curr.next
    curr.next = prev 
    prev = curr
    curr = next
  head.next = kReverse(curr, k)
  return prev 
    
    
  





head = take_input()
new_head = kReverse(head,4)
print_ll(new_head)

