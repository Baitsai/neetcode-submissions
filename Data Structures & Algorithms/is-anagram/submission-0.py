class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for c in s:
            # 如果c已經在hashmap裡，就拿出原本的數量
            # 如果c不在hashmap裡，就先當作0
            # hashmap[c] = hashmap.get(c,0) + 1
            if c in hashmap:
                hashmap[c] = hashmap[c] + 1
            else:
                hashmap[c] = 1

        for c in t:
            if c not in hashmap:
                return False

            hashmap[c] -= 1
            if hashmap[c] < 0:
                return False

        return True

        