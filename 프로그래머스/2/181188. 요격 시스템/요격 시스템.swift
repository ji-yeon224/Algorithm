import Foundation

func solution(_ targets:[[Int]]) -> Int {
    
    var targets = targets
    targets.sort {
        if $0[0] == $1[0] {
            return $0[1]<$1[1]
        } else {
            return $0[0] < $1[0]
        }
    }
    var answer = 0
    var start = targets[0][0]
    var end = targets[0][1]
    for i in 1..<targets.count {
        var cur = targets[i]
        if end <= cur[0] {
            answer += 1
            start = cur[0]
            end = cur[1]
        } else {
            end = min(end, cur[1])
        }
    }
    
    
    return answer + 1
}