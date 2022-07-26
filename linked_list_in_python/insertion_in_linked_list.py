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

head = take_input()
head = insertion_at_ith_position(head,lenght_of_ll(head),99)
print_ll(head)i
