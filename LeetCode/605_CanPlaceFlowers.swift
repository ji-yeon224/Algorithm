class Solution {
    
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        
        
        var count = 1
        var bed = 0
        
        for flower in flowerbed {
            if flower == 1 {
                bed += (count - 1) / 2
                count = 0
            } else {
                count += 1
            }
        }
        if count != 0 {
            bed += count / 2
        }
        print(bed)
        
        return bed >= n
    }
    
    
}