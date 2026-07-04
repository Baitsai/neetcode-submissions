class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        //unordered_set<int> 只能記錄「有沒有出現」，不能記錄次數
        //需要記錄字母出現次數，所以用 unordered_map<char, int>
        unordered_map<char, int> hashmap;
        for(char c:s)hashmap[c]++;

        for (char c : t) {
            hashmap[c]--;
            if (hashmap[c] < 0) return false;
        }
        return true;
    }
};
