class Solution(object):
    def isStackEmpty(self, A):
        if len(A) == 0:
            return True
        return False
    def countInvalidParanethesis(self, A):
        stack = []
        for ch in A:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if self.isStackEmpty(stack):
                    stack.append(ch)
                else:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(ch)
        return len(stack)
    def generateAllValidParathesis(self, A, ans, current, charRemoved, cntInvParanthesis, seen):
        if current in seen:
            return
        else:
            seen.add(current)
        # if charRemoved > cntInvParanthesis:
        #     return
        if charRemoved == cntInvParanthesis:
            if self.countInvalidParanethesis(current) == 0:
                res = ''+current
                ans.add(res)
            return
        for i in range(0, len(current)):
            a = current[:i]
            b = current[i+1:]
            new = a+b
            self.generateAllValidParathesis(A, ans, new, charRemoved+1, cntInvParanthesis, seen)
    def removeInvalidParentheses(self, A):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(A) == 0:
            return list(ans)
        cntInvParanthesis = self.countInvalidParanethesis(A)
        ans = set()
        seen = set()
        charRemoved = 0
        current = ''+A
        self.generateAllValidParathesis(A, ans, current, charRemoved, cntInvParanthesis, seen)
        return list(ans)
        