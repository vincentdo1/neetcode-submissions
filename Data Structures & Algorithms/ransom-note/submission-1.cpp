class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int>magazineMap;
        for (char ch : magazine) {
            magazineMap[ch]++;
        }
        for (char ch : ransomNote) {
            if (magazineMap[ch] == 0) {
                return false;
            } else {
                magazineMap[ch]--;
            }
        }
        return true;
    }
};