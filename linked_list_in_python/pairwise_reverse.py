def reverse_a_ll_pairwise(head):
  if head == None or head.next == None:
    return head
  temp = head.next
  head.next = reverse_a_ll_pairwise(head.next.next)
  temp.next = head
  return temp

