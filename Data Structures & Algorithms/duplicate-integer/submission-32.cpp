using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::unordered_set<int> elements;
        for(const auto& num: nums){
            if(elements.contains(num)){
                return true;
            }
            elements.insert(num);

            cout << num ;
            
        }

        return false;

        
        
    }
};