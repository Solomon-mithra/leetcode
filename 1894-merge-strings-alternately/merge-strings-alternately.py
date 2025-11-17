class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) > len(word2):
            maxType = word1
            maxNum = len(word2)
            diff = len(word1) - len(word2)
        else:
            maxType = word2
            maxNum = len(word1)
            diff = len(word2) - len(word1)
        print(maxNum)
        print(diff)
        final = ''
        for i in range(0,maxNum):
            final = final+word1[i]+word2[i]
        for i in range(0,diff):
            final = final + maxType[i+maxNum]  
        return final
        
        