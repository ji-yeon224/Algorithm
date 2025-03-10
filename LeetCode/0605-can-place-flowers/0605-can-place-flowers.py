class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plantingCount = 0
        if n == 0:
            return True
        index = 0
        while index < len(flowerbed):
            if flowerbed[index] == 1:
                index += 2
            else:
                if index < len(flowerbed)-1 and flowerbed[index+1] != 1:
                    plantingCount += 1
                    index += 2
                elif index == len(flowerbed)-1:
                    plantingCount += 1
                    break
                else:
                    index += 1
        
        return plantingCount >= n


