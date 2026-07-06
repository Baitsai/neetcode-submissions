class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        jump = []
        for idx0 in range (len(strs)):
            if idx0 not in jump :
                hashmap = {}
                a = []
                for s in strs[idx0]:
                    if s in hashmap:
                        hashmap[s] = hashmap[s] + 1
                    else:
                        hashmap[s] = 1
                flag = 1
                for idx1 in range (idx0+1, len(strs)):
                    if idx1 not in jump :

                        hashmap1 = hashmap.copy()
                        #hashmap1 = hashmap 讓 hashmap1 和 hashmap 指向同一個 dictionary
                        if len(strs[idx1]) != len(strs[idx0]):
                            continue
                        flag = 1
                        for c in strs[idx1]:
                            if c in hashmap1:
                                hashmap1[c] = hashmap1[c] - 1
                            if (c not in hashmap):
                                flag = 0
                                break
                        for key in hashmap1:
                            if hashmap1[key] < 0:
                                flag = 0
                        if flag:
                            jump.append(idx1)
                            a.append(strs[idx1])
                a.append(strs[idx0])
                ans.append(a)
                
        return ans
