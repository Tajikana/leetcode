class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        
        way=[0] *(n+1)

        way[2]=2
        way[1]=1
        
        for i in range(3,n+1):

            way[i]=way[i-1] +way[i-2] 

        return way[n]
        
