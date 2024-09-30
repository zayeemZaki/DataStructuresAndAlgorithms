class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""

        i=0
        while i < len(chars):
            temp = chars[i]

            count = 0
            while i < len(chars) and chars[i] == temp:
                count += 1
                i += 1

            s += temp
            if count > 1:
                s += str(count)

            
        chars[:len(s)] = s

        return len(s)