class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointer1, pointer2 = headA, headB

        while pointer1 != pointer2:
            if pointer1:
                pointer1 = pointer1.next
            else:
                pointer1 = headB
            
            if pointer2:
                pointer2 = pointer2.next
            else:
                pointer2 = headA
        
        return pointer1