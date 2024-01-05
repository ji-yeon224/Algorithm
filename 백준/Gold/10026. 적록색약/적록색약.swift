import Foundation

typealias Index = (r: Int, c: Int)

func solution() {
    
    
    let n = Int(readLine()!)!
    
    var grid: [[String]] = []
    var visited: [[Bool]] = Array.init(repeating: Array.init(repeating: false, count: n), count: n)
    var rgVisited: [[Bool]] = Array.init(repeating: Array.init(repeating: false, count: n), count: n)
    
    var colorArea: Int = 0
    var rgColorArea: Int = 0
    
    for _ in 0..<n {
        let line = readLine()!.map { "\($0)" }
        grid.append(line)
    }
    
    
    let dir: [Index] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    func isPossibleWay(idx: Index) -> Bool {
        if idx.r >= 0 && idx.r < n && idx.c >= 0 && idx.c < n {
            return true
        } else { return false }
    }
    
    
    
    func bfs(_ start: Index, _ color: String, queue: [Index], _ rg: Bool) {
        
        var queue = queue
        queue.append(start)
        while !queue.isEmpty {
            
            let curIdx = queue.removeFirst()
            dir.forEach {
                let nxt: Index = (curIdx.r + $0.r, curIdx.c + $0.c)
                if isPossibleWay(idx: nxt) { // 이동 가능함
                    let nxtColor = grid[nxt.r][nxt.c]
                    if rg {
                        if !rgVisited[nxt.r][nxt.c] {
                            if (color == "R" && nxtColor == "G") || (color == "G" && nxtColor == "R" ) || color == nxtColor {
                                queue.append(nxt)
                                rgVisited[nxt.r][nxt.c] = true
                            }
                        }
                        
                    } else {
                        if !visited[nxt.r][nxt.c] && color == nxtColor {
                            queue.append(nxt)
                            visited[nxt.r][nxt.c] = true
                        }
                    }
                }
                
                
            }
            
            
        }
       
        
        
    }
    var normalQueue: [Index] = []
    var rgQueue: [Index] = []
    for i in 0..<n {
        for j in 0..<n {
            if !visited[i][j] {
                visited[i][i] = true
                bfs((i, j), grid[i][j], queue: normalQueue, false)
                colorArea += 1
            }
            if !rgVisited[i][j] {
                rgVisited[i][j] = true
                bfs((i, j), grid[i][j], queue: rgQueue, true)
                rgColorArea += 1
            }
        }
    }
    
    print(colorArea, rgColorArea)
}

solution()
