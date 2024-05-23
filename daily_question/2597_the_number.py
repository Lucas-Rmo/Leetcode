class Solution(object):
    def beautifulSubsets(self, nums, k):
        M = 10**9 + 7
        
        n = len(nums)
        nums.sort()
        
        dic = {}
        fre = {}

        for num in nums:
            if num not in fre:  fre[num] = 0
            fre[num] += 1

            if num % k not in dic:  dic[num%k] = []
            if fre[num] == 1:   dic[num%k].append(num//k)
        
        ans = 1
        
        for key in dic:
            temp = dic[key]
            dp = [0]*len(temp) + [1]
            dp[0] = pow(2,fre[key+temp[0]*k],M)

            for i in range(1,len(temp)):

                dp[i] += dp[i-1]
                if temp[i]==temp[i-1] + 1:
                    dp[i] +=  dp[i-2] * (pow(2,fre[key+temp[i]*k],M) - 1)
                else:
                    dp[i] += dp[i-1] * (pow(2,fre[key+temp[i]*k],M) - 1)
                    
                dp[i] %= M
                    
            ans *= dp[len(temp)-1]
            ans %= M

        return (ans - 1)%M
