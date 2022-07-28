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
    return head2
  if head2 == None:
    return head2
  return curr.next
