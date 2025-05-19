import Foundation

struct Queue<T> {
    private var inbox: [T] = []
    private var outbox: [T] = []
    
    var isEmpty: Bool {
        inbox.isEmpty && outbox.isEmpty
    }
    
    mutating func enqueue(_ value: T) {
        inbox.append(value)
    }
    mutating func dequeue() -> T {
        if outbox.isEmpty {
            outbox = inbox.reversed()
            inbox.removeAll()
        }
        return outbox.popLast()!
    }
}

let N = Int(readLine()!)!
var area: [[Int]] = []
var maxHeight = 0
let dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
var visitedInit = Array(repeating: Array(repeating: false, count: N), count: N)

for _ in 0..<N {
    let items = readLine()!
        .split(separator: " ")
        .compactMap{ Int($0) }
    area.append(items)
    let maxNum = items.max()!
    maxHeight = max(maxHeight, maxNum)
}

func bfs(_ start: (Int, Int), height: Int) {
    var queue = Queue<(Int, Int)>()
    queue.enqueue(start)
    visited[start.0][start.1] = true
    
    while !queue.isEmpty {
        let (curR, curC) = queue.dequeue()
        dir.forEach { (dr, dc) in
            let (nr, nc) = (curR+dr, curC + dc)
            if nr >= 0, nr < N, nc >= 0, nc < N, !visited[nr][nc], area[nr][nc] >= height {
                queue.enqueue((nr, nc))
                visited[nr][nc] = true
            }
        }
        
    }
}

var visited: [[Bool]] = []
var answer = 0

for height in 0...maxHeight {
    visited = visitedInit
    var result = 0
    for i in 0..<N {
        for j in 0..<N {
            if area[i][j] >= height, !visited[i][j] {
                bfs((i, j), height: height)
                result += 1
            }
        }
    }
    
    answer = max(answer, result)
}
print(answer)
