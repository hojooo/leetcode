class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global dic
        global ans
        global j

        dic = {}
        ans = 0
        j = 0

        def diffDic(c):
            global ans
            global j
            
            while dic[c] > 1:       # O(n)
                if dic[s[j]] > 1:
                    dic[s[j]] -= 1
                else:
                    del dic[s[j]]
                    
                j += 1


        for i in s:     # O(n)
            if i not in dic:
                dic[i] = dic.get(i, 0) + 1
            else:
                dic[i] += 1
                diffDic(i)
            
            if len(dic) > ans:
                ans = len(dic)

        return ans      