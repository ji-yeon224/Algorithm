import Foundation

final class FileIO {
    private let buffer:[UInt8]
    private var index: Int = 0

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        
        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer[index]
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10
                || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45 { isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> String {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시

        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return String(bytes: Array(buffer[beginIndex..<(index-1)]), encoding: .ascii)!
    }

    @inline(__always) func readByteSequenceWithoutSpaceAndLineFeed() -> [UInt8] {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시

        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return Array(buffer[beginIndex..<(index-1)])
    }
}

typealias Tomato = (h: Int, r: Int, c: Int, d: Int)

struct Queue {
    private var queue: [Tomato] = []
    var front = 0
    
    var isEmpty: Bool {
        return front >= queue.count
    }
    var count: Int {
        return queue.count
    }
    mutating func enqueue(_ element: Tomato) {
        queue.append(element)
    }
    mutating func dequeue() -> Tomato {
        let cur = queue[front]
        front += 1
        return cur
    }
}
let fileIO = FileIO()


func solution() -> Int {
    
    var zeroCnt = 0
    var queue = Queue()
    let col = fileIO.readInt()
    let row = fileIO.readInt()
    let height = fileIO.readInt()
    
    var box: [[[Int]]] = Array.init(repeating: Array.init(repeating: Array.init(repeating: 0, count: col), count: row), count: height)
    
    for h in 0..<height {
        for r in 0..<row {
            for c in 0..<col {
                box[h][r][c] = fileIO.readInt()
            }
        }
    }
    
    
    for h in 0..<height {
        for r in 0..<row {
            for c in 0..<col {
                if box[h][r][c] == 1 {
                    queue.enqueue((h,r,c, 0))
                }
                else if box[h][r][c] == 0{
                    zeroCnt += 1
                }
            }
        }
    }
    
   
    if zeroCnt == 0 {
        return 0
    }
    if queue.count == 0 {
        return -1
    }
    
    func isPossibleWay(_ idx: (Int, Int, Int)) -> Bool {
        
        let(h, r, c) = idx
        if 0..<height ~= h && 0..<row ~= r && 0..<col ~= c && box[h][r][c] == 0 {
            zeroCnt -= 1
            return true
        } else {
            return false
        }
        
    }
    
    let dir = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    var maxDay = 0
    func bfs() {
        while !queue.isEmpty {
            
            let cur = queue.dequeue()
            dir.forEach {
                let nh = cur.h+$0.0, nr = cur.r+$0.1, nc = cur.c+$0.2, d = cur.d
                
                if isPossibleWay((nh, nr, nc)) {
                    queue.enqueue((nh, nr, nc, d+1))
                    box[nh][nr][nc] = d + 1
                    maxDay = max(maxDay, d+1)
                }
            }
        }
        
    }
   
    bfs()
    if zeroCnt != 0 {
        return -1
    }
    return (box.flatMap{ $0 }.flatMap { $0 }.max()!)
    
}


print(solution())
