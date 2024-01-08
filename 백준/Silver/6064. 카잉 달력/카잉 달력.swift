import Foundation

func gcd(_ a: Int, _ b : Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a % b)
    }
}

func lcm(_ a: Int, _ b: Int) -> Int {
    return a * b / gcd(a, b)
}
var result: [Int] = []
func solution() -> Int {
    
    let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
    let n = input[0], m = input[1]
    let dstN = input[2], dstM = input[3]
    
    let max = lcm(n, m)
    if n == dstN && m == dstM {
        return max
    }
    
    var result = -1
    
    var isPossible = false
    for i in 0..<max / n {
        
        let year = i * n + dstN
        let curM = year % m  == 0 ? m : year % m
        if curM == dstM {
            isPossible = true
            result = year
            break
        }
        
        
    }
    
    
    return isPossible ? result : -1
}

let cnt = Int(readLine()!)!
for _ in 0..<cnt {
    result.append(solution())
}
_ = result.map { print($0) }