using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        if(nums.size() < 2){
            return false;
        }
        
        vector<int> copy;
        copy = nums;

        sort(copy.begin(), copy.end());

        for(int i = 1; i < nums.size(); i++){
            if (copy[i] == copy[i - 1]){
                return true;
            }

        }
        
        
        return false;


        
        
    }
};