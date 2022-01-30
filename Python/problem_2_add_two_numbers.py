# Definition for singly-linked list
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution():
    root = None
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = int(self.traverse(l1))
        num2 = int(self.traverse(l2))
        result = str(num1+num2)
        print(result)
        for i in range(len(result)):
            self.append(result[i])
            
    
    def traverse(self, ll):
        ptr, res = ll, ''
        while ptr:
            res += str(ptr.val)
            ptr = ptr.next
        return res[::-1]
            
    
    def append(self, val):
        node  = ListNode()
        node.val = val
        if self.root is None:
            self.root = node
            return
        ptr = self.root
        while ptr.next:
            ptr = ptr.next
        ptr.next = node
        

# driver code
node  = Solution()
node.append(2)
node.append(4)
node.append(3)

ptr = Solution()
ptr.append(5)
ptr.append(6)
ptr.append(4)

a = node.traverse(node.root)
b = ptr.traverse(ptr.root)
print(a)
print(b)

res = Solution()
res.addTwoNumbers(node.root, ptr.root)
print(res.traverse(res.root))