class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        output_str = ''
        for char in S:
            if not self.is_digit(char):
                output_str += char
            else:
                rep = int(char)
                current_str = output_str
                for idx in range(rep-1):
                    output_str = output_str + current_str 
                    if len(output_str) >= K:
                        print(output_str)
                        return output_str[K-1]
        print(output_str)
        return output_str[K-1]
    
    # check digit or letter
    def is_digit(self, str):
        ascii = ord(str)
        if ascii >= 48 and ascii <= 57:
            return True
        return False
    
str1 = 'leet2code3'
K1 = 10
str2 = 'ha22'
K2 = 5
str3 = 'a2345678999999999999999'
K3 = 1
str4 = 'y959q969u3hb22'#odq595'
K4 = 2367810
#K4 = 222280369

s = Solution()
print(K1, s.decodeAtIndex(str1, K1))
print(K2, s.decodeAtIndex(str2, K2))
print(K3, s.decodeAtIndex(str3, K3))
print(K4, s.decodeAtIndex(str4, K4))