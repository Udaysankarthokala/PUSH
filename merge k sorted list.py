import heapq

def mergeKLists(lists):

    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap,
                          (lst.val, i, lst))

    dummy = ListNode(0)
    current = dummy

    while heap:

        value, i, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(
                heap,
                (node.next.val,
                 i,
                 node.next)
            )

    return dummy.next