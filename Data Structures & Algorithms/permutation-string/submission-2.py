class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
            
        l,r=0,len(s1)-1
        while r < len(s2)-1:
            if matches == 26:
                return True
            else:
                r+=1
                index = ord(s2[r])-ord("a")
                count2[index] += 1
                if count2[index] == count1[index]:
                    matches += 1
                if count2[index] == count1[index] + 1:
                    matches -= 1

                index = ord(s2[l])-ord("a")
                count2[index] -= 1
                if count2[index] == count1[index]:
                    matches += 1
                if count2[index] +1 == count1[index]:
                    matches -= 1
                l+=1

        return matches == 26

    