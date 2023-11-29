import Foundation

func solution(_ x:Int, _ y:Int, _ n:Int) -> Int {
    
    if x == y {
        return 0
    }
    
    let destNum = x
    
    var queue: [(Int, Int)] = [] // 현재 숫자, 연산 횟수
    queue.append((y,0))
    
    while !queue.isEmpty {
        
        let cur = queue.removeFirst()
        let curNum = cur.0
        let cnt = cur.1
        if curNum == destNum { // 목표 값에 도달하면
            return cnt
        } else if curNum < destNum {
            continue
        }
        
        if curNum % 2 == 0 {
            queue.append((curNum/2, cnt+1))
        }
        if curNum % 3 == 0 {
            queue.append((curNum/3, cnt+1))
        }
        queue.append((curNum-n, cnt+1))
    }
    
    return -1
}