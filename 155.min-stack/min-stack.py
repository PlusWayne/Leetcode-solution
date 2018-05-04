class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min=self.getMin()
        if cur_min== None or x<cur_min:  # the first is satisfied, then it won't check the second term
            cur_min=x
        self.q.append((x,cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1][0] if len(self.q)!=0 else None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return None
        else:
            return self.q[-1][1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
