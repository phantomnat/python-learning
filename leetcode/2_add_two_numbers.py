class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        pl1 = l1
        pl2 = l2
        carry_add = 0
        head = ListNode(0)
        ans_p = None
        while not (pl1 is None and pl2 is None):
            v = carry_add
            if pl1 is not None:
                v += pl1.val
                pl1 = pl1.next
            if pl2 is not None: 
                v += pl2.val
                pl2 = pl2.next

            val = (v - 10) if v >= 10 else v

            if ans_p is None:
                head.val = val
                ans_p = head
            else:
                ans_p.next = ListNode(val)
                ans_p = ans_p.next

            carry_add = 1 if v >= 10 else 0

        if carry_add == 1:
            ans_p.next = ListNode(1)

        return head

    def listToInt(self, ln):
        num = 0
        dep = 1
        while True:
            num += dep * ln.val
            if ln.next is None:
                break
            dep *= 10
            ln = ln.next
        return num
    
    def intToList(self, val):
        head = ListNode(0)
        ln = None
        while True:
            print_list(head)
            if (val <= 0):
                break
            last_digit = val % 10
            if ln is None:
                head.val = last_digit
                ln = head
            else:
                ln.next = ListNode(last_digit)
                ln = ln.next
            val = val // 10
        return head

def print_list(l):
    while True:
        print(l.val, end='')
        if l.next is None:
            print('')
            break
        print(' -> ', end='')
        l = l.next

if __name__ == '__main__':

    c = Solution()

    
    a = c.intToList(1)
    b = c.intToList(999)
    print_list(a)
    print_list(b)


    d = c.addTwoNumbers(a, b)
    print_list(d)
