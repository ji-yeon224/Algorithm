import Foundation

typealias Index = (r: Int, c: Int)

struct Queue {
    private var queue: [Index] = []
    var front = 0

    var isEmpty: Bool {
        return front >= queue.count
    }
    var count: Int {
        return queue.count
    }
    mutating func enqueue(_ element: Index) {
        queue.append(element)
    }
    mutating func dequeue() -> Index {
        let cur = queue[front]
        front += 1
        return cur
    }
}

func solution() {
   
    let size = readLine()!.components(separatedBy: " ").map { Int($0)! }
    let row = size[0]
    let col = size[1]
    
    var map: [[Int]] = []
    var destIdx: Index = (0, 0)
    var distance: [[Int]] = Array.init(repeating: Array.init(repeating: -1, count: col), count: row)
    var visited: [[Bool]] = Array.init(repeating: Array.init(repeating: false, count: col), count: row)
    
    for i in 0..<row {
        let line = readLine()!.components(separatedBy: " ").map { Int($0)! }
        for j in 0..<col {
            if line[j] == 0 {
                distance[i][j] = 0
            } else if line[j] == 2 {
                destIdx = (i, j)
            }
        }
            
        map.append(line)
    }
    
    func bfs() {
        let dir: [Index] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        var queue = Queue()
        queue.enqueue(destIdx)
        distance[destIdx.r][destIdx.c] = 0
        visited[destIdx.r][destIdx.c] = true
        while !queue.isEmpty {
            let cur = queue.dequeue()
            let dis = distance[cur.r][cur.c]
            dir.forEach {
                let nxt: Index = (cur.r + $0.r, cur.c + $0.c)
                if nxt.r >= 0 && nxt.r < row && nxt.c >= 0 && nxt.c < col && !visited[nxt.r][nxt.c] {
                    if map[nxt.r][nxt.c] == 0{
                        distance[nxt.r][nxt.c] = 0
                    } else {
                        queue.enqueue(nxt)
                        distance[nxt.r][nxt.c] = dis + 1
                    }
                    visited[nxt.r][nxt.c] = true
                }
            }
        }
        
    }
    
    bfs()
    distance.forEach { arr in
        var line = ""
        line = arr.map { "\($0)" }.joined(separator: " ")
        print(line)
    }
}
solution()