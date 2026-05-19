class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_list = []
        encoded_str = []
        #n
        for s in strs:
            if(s == ""):
                encoded_str.append("x ")
            else:
            
                encoded_list = [ord(char) for char in s]
                #m
                for number in encoded_list:
                    # m*n space?
                    encoded_str.append(str(number))
                    encoded_str.append(",")
                
                encoded_str = encoded_str[:-1]
                encoded_str.append(" ")
        

        return "".join(encoded_str)
                

    def decode(self, s: str) -> List[str]:
        splited = s.split()
        decoded_list = []
        decoded_str = ""
        for number in splited:
            if (number == 'x'):
                decoded_str = ""
            else:
                digits = number.split(',')
                for digit in digits:
                    print(digit)
                    print(type(digit))
                    decoded_str += chr(int(digit))


            decoded_list.append(decoded_str)
            decoded_str = ""

        return decoded_list
            

            
