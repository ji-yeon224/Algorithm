import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    
    var queue:[Int] = []
    var jobCnt = progresses.count
    for i in 0..<jobCnt {
        var work = 100 - progresses[i]
        var time = work/speeds[i]
        if work%speeds[i] > 0 {
            time += 1
        }
        queue.append(time)
    }
    
    var answer: [Int] = []
    var prevMax: Int = queue.removeFirst()
    var cnt = 1
    while !queue.isEmpty {
        let finish = queue.removeFirst()
        if finish > prevMax {
            answer.append(cnt)
            cnt = 1
            prevMax = finish
        } else {
            cnt += 1
        }
    }
    answer.append(cnt)
    
    return answer
}