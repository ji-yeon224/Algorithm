import Foundation


func solution() -> Int {
    
    let meeting = Int(readLine()!)!

    var meetings: [(Int, Int)] = []
    var maxCnt = 1
    for _ in 0..<meeting {
        let time = readLine()!.components(separatedBy: " ").map { Int($0)! }
        meetings.append((time[0], time[1]))
    }
    
    meetings.sort {
        if $0.1 == $1.1 {
            return $0.0 < $1.0
        }
        return $0.1 < $1.1
    }
    
    var last = -1
    var result = 0
    for m in meetings {
        let (start, end) = m
        if start >= last {
            result += 1
            last = end
        }
    }
   
    
    return result
}

print(solution())
