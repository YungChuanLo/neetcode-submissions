using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> set_s;
        unordered_map<char, int> set_t;

        for(auto c : s){
            set_s[c]++;
        }
        for(auto c : t){
            set_t[c]++;
        }

        return set_s == set_t;


        
        
    }
};
