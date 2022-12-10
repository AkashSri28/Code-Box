#User function Template for python3

class Solution:
    def primeDivision(self, A):
        # code here
        sieve = [True for i in range(A+1)]
        for i in range(2, A+1):
            if(sieve[i]):
                for j in range(i*i, A+1, i):
                    if(sieve[j]):
                        sieve[j] = False
        for i in range(2, A):
            if sieve[i] and sieve[A-i]:
                ans = [i, A-i]
                break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends