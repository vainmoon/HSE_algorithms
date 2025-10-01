class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def merge_lists(list1, list2):
    merged_head = None

    if not list1:
        return list2
    if not list2:
        return list1

    if list1.value < list2.value:
        merged_head = list1
        list1 = list1.next
    else:
        merged_head = list2
        list2 = list2.next

    merged_tail = merged_head

    while list1 and list2:
        if list1.value < list2.value:
            merged_tail.next = list1
            list1 = list1.next
        else:
            merged_tail.next = list2
            list2 = list2.next
        merged_tail = merged_tail.next

    merged_tail.next = list1 if list1 else list2

    return merged_head
