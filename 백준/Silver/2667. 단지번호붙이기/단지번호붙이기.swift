import Foundation

let length = Int(readLine()!)!
let dir: [(Int, Int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

func solution() {
    
    var map: [[Int]] = []
    
    var visited = Array(repeating: Array(repeating: false, count: length), count: length)
    
    for _ in 0..<length {
        map.append(String(readLine()!).map { Int("\($0)")! })
    }
    
    func bfs(_ cur: (Int, Int)) -> Int {
        var count = 1
        var queue: [(Int, Int)] = []
        queue.append(cur)
        while !queue.isEmpty {
            let cur = queue.removeFirst()
            
            dir.forEach {
                
                let nxtRow = cur.0 + $0.0, nxtCol = cur.1 + $0.1
                if nxtRow >= 0 && nxtCol >= 0 && nxtRow < length && nxtCol < length && !visited[nxtRow][nxtCol] && map[nxtRow][nxtCol] == 1 {
                    queue.append((nxtRow, nxtCol))
                    visited[nxtRow][nxtCol] = true
                    count += 1
                }
                
            }
            
        }
        
        return count
        
    }
    
    var results: [Int] = []
    for (row, arr) in map.enumerated() {
        for (col, value) in arr.enumerated() {
            if !visited[row][col] && value == 1 {
                visited[row][col] = true
                let cnt = bfs((row, col))
                results.append(cnt)
            }
        }
    }
    
    results.sort(by: <)
    print(results.count)
    results.forEach { print($0) }
    
   
}


solution()