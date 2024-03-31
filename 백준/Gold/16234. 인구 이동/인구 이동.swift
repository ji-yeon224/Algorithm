struct Queue {
    var queue: [Idx] = []
    var front = 0
    
    var isEmpty: Bool {
        return front >= queue.count
    }
    
    mutating func enqueue(_ idx: Idx) {
        queue.append(idx)
    }
    
    mutating func dequeue() -> Idx {
        let data = queue[front]
        front += 1
        return data
    }
}

let inputArr: [Int] = readLine()!.split(separator: " ").map {Int($0)!}

let N = inputArr[0]
let L = inputArr[1]
let R = inputArr[2]
var visited: [[Bool]] = []
typealias Idx = (r: Int, c: Int)

var map: [[Int]] = Array(repeating: [], count: N)
for i in 0..<N {
    let line: [Int] = readLine()!.split(separator: " ").map {Int($0)!}
    map[i] = line
}



func bfs(_ start: Idx) -> Bool {
    var union: [Idx] = []
    var queue = Queue()
    let dir: [Idx] = [Idx(-1, 0), Idx(1, 0), Idx(0, -1), Idx(0, 1)]
    var totalCnt = 0
    
    queue.enqueue(start)
    visited[start.r][start.c] = true
    
    while !queue.isEmpty {
        let cur = queue.dequeue()
        let curCnt = map[cur.r][cur.c]
        union.append(cur)
        totalCnt += map[cur.r][cur.c]
        
        dir.forEach { d in
            let nxtR = cur.r + d.r
            let nxtC = cur.c + d.c
            
            if 0..<N ~= nxtR && 0..<N ~= nxtC && !visited[nxtR][nxtC] && L...R ~= abs(curCnt - map[nxtR][nxtC]) {
                queue.enqueue(Idx(nxtR, nxtC))
                visited[nxtR][nxtC] = true
            }
        }
    }
    
    if union.count > 1 {
        let moveCnt = totalCnt / union.count
        union.forEach {
            map[$0.r][$0.c] = moveCnt
        }
        return true
    } else { return false }
}

func solution() {
    
    var day = 0
    while true {
        var move = 0
        visited = Array(repeating: Array(repeating: false, count: N), count: N)
        for i in 0..<N {
            for j in 0..<N {
                if !visited[i][j] {
                    if bfs(Idx(i, j)) {
                        move += 1
                    }
                    
                }
            }
        }
        
        
        if move == 0 {
            break
        } else {
            day += 1
        }
    }
    print(day)
    
}


solution()
