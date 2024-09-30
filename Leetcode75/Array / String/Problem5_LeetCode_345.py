class Solution:
    def reverseVowels(self, s: str) -> str:

        arr = list(s)
        i, j = 0, len(arr)-1

        while i < j:
            while i < j and not self.isVowel(s[i]):
                i += 1
            while i < j and not self.isVowel(s[j]):
                j -= 1
            
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j -= 1
        
        return ''.join(arr)

    def isVowel(self, ch: chr) -> bool:
        ch = ch.lower()

        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            return True
        else:
            return False        
