class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(f"{len(word)}#{word}")

        print(result)
        
        return "".join(result)
            

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 1
        str_list = []
        while(right < len(s)):
            
            if(s[right] == "#"):
                print(left)
                print(right)
                
                length = int(s[left:right])
                str_list.append(s[right + 1:right + 1 + length])
                left = right + 1 + length
                right = right + 1 + length
            else:
                right += 1
        return str_list

            
                
