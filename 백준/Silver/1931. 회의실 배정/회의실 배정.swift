import Foundation


func solution() -> Int {
    
    let meeting = Int(readLine()!)!

    var meetings: [(Int, Int)] = []
    var maxCnt = 1
    for _ in 0..<meeting {
        let time = readLine()!.components(separatedBy: " ").map { Int($0)! }
        meetings.append((time[0], time[1]))
    }

    // 종료 시간이 빠른 순
    meetings.sort {
        if $0.1 == $1.1 { // 종료 시간이 같다면 시작 시간이 빠른 순
            return $0.0 < $1.0
        }
        return $0.1 < $1.1
    }

    // 첫 번째 회의실이 가장 많이 들어가는 회의실
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
