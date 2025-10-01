class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def dummy_merge_lists(list1, list2):
    dummy_node = ListNode()
    merged_tail = dummy_node

    while list1 and list2:
        if list1.value < list2.value:
            merged_tail.next = list1
            list1 = list1.next
        else:
            merged_tail.next = list2
            list2 = list2.next
        merged_tail = merged_tail.next

    merged_tail.next = list1 if list1 else list2

    return dummy_node.next
