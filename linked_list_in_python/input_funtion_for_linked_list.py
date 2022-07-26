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


    

head = take_input()
print_ll(head)
