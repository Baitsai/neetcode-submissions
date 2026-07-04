class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashmap;
        for(int num : nums){
            if(hashmap.count(num)) return true;
            hashmap.insert(num);
        }
        return false;
    }
};