import Foundation

func solution(_ weights:[Int]) -> Int64 {
    
    var result = 0
    
    var map: [Double: Int] = [:] // 몸무게 : 인원
    
    for weight in weights {
        map[Double(weight), default: 0] += 1
    }
    
    let keys = map.keys.sorted()
    for key in keys {
        let count = map[key]!
        if count > 1 {
            result += (count * (count - 1) / 2)
        }
        
        
        for i in 1..<4 {
            let mate = key * Double(i) / Double(i+1)
            if let cnt = map[mate] {
                
                result += (cnt * count)
            }
        }
    }
    
    return Int64(result)
}