from dummy_merge_lists import ListNode, dummy_merge_lists
from merge_lists import merge_lists
import pytest


def get_linked_list(list):
    if not list:
        return None

    head = ListNode(list[0])
    current_node = head
    for value in list[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return head


def get_list(head):
    list = []
    current_node = head
    while current_node:
        list.append(current_node.value)
        current_node = current_node.next
    return list


@pytest.mark.parametrize("merge_lists_func", [dummy_merge_lists, merge_lists])
@pytest.mark.parametrize(
    "list1, list2, merged_list",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1], [1, 2, 3], [1, 1, 2, 3]),
        ([], [0], [0]),
        ([], [], []),
        ([5, 10], [1, 2, 5, 8, 19, 20], [1, 2, 5, 5, 8, 10, 19, 20]),
    ],
)
def test_merge_lists(merge_lists_func, list1, list2, merged_list):
    result = merge_lists_func(get_linked_list(list1), get_linked_list(list2))
    result = get_list(result)
    assert result == merged_list
