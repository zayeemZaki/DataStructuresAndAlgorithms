class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            if n == 0:
                return True

            left, right = True, True

            if i == 0 or flowerbed[i-1] == 0:
                left = False
            if i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                right = False

            if not left and not right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return True if n == 0 else False