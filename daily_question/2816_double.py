class Solution:
   #copei e colei o codigo,preciso estudar mais
    def twice_of_val(self, head: Optional[ListNode]) -> int:
     
        if not head:
            return 0
        
       
        doubled_value = head.val * 2 + self.twice_of_val(head.next)
        
        
        head.val = doubled_value % 10
        
    
        return doubled_value // 10
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.twice_of_val(head)
        

        if carry:
            head = ListNode(carry, head)
        
        return head281
