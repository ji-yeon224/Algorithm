import Foundation

struct Queue {
    private var queue: [Int] = []
    var front = 0

    var isEmpty: Bool {
        return front >= queue.count
    }
    var count: Int {
        return queue.count
    }
    mutating func enqueue(_ element: Int) {
        queue.append(element)
    }
    mutating func dequeue() -> Int {
        let cur = queue[front]
        front += 1
        return cur
    }
}


func solution() {
    
    let input = readLine()!.components(separatedBy: " ").map{ Int("\($0)")! }
    let ladderCnt = input[0]
    let snakeCnt = input[1]
    
    var snakeLadder: [Int: Int] = [:]
    for _ in 0..<ladderCnt+snakeCnt {
        let input = readLine()!.components(separatedBy: " ").map{ Int("\($0)")! }
        snakeLadder[input[0]] = input[1]
    }
    
    var visited: [Int] = Array.init(repeating: 0, count: 101)
    
    var queue = Queue()
    queue.enqueue(1)
    
    while !queue.isEmpty {
        let cur = queue.dequeue()
        let cnt = visited[cur]
        
        if cur == 100 && cnt != 0 {
            break
        }
        for i in 1...6 {
            var nxt = cur + i
            if nxt <= 100 {
                if snakeLadder[nxt] != nil {
                    nxt = snakeLadder[nxt]!
                }
                if visited[nxt] == 0 || ( visited[nxt] > 0 && visited[nxt] < cnt ) { // 방문한 적 없거나 방문 횟수가 더 적으면
                    queue.enqueue(nxt)
                    visited[nxt] = cnt + 1
                }
            }
        }
        
    }
    
    print(visited[100])
    
}

solution()