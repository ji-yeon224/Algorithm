import Foundation

func solution(_ scores:[[Int]]) -> Int {
    var answer = 1
    var wanho = scores[0]
    var wScore = wanho[0] + wanho[1]
    
    var scores: [[Int]] = scores.sorted {
        return $0[0] == $1[0] ? $0[1] < $1[1] : $0[0] > $1[0]
    }
    var maxNum = scores[0][1]
    
    for s in scores {
        if maxNum > s[1] {
            if s == wanho { 
                answer = -1
                break
            }
        } else {
            if s[0]+s[1] > wScore {
                answer += 1
            }
            maxNum = max(maxNum, s[1])
        }
    }
    
    return answer
}