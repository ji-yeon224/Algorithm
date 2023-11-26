import Foundation

func solution(_ maps:[String]) -> [Int] {
    
    var maps = maps.map{ $0.map{String($0)}}
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, 1, -1]
    var visited: [[Bool]] =  Array(repeating: Array(repeating: false, count: maps[0].count), count: maps.count)
    var result:[Int] = []
    
    
    var queue: [(Int, Int)] = []
    func bfs(_ x: Int, _ y: Int, _ sum: Int) -> Int {
        var sum = sum
        while !queue.isEmpty {
            let cur = queue.removeFirst()
            for i in 0..<4 {
                let nx = cur.0 + dx[i]
                let ny = cur.1 + dy[i]
                if nx >= 0 && nx < maps.count && ny >= 0 && ny < maps[0].count {
                    if !visited[nx][ny] && maps[nx][ny] != "X" {
                        sum += Int(maps[nx][ny])!
                        visited[nx][ny] = true
                        queue.append((nx, ny))
                    }
                }
            }
            
        }
        return sum
        
    }
    
    for (x, row) in maps.enumerated() {
        for (y, value) in row.enumerated() {
            if !visited[x][y] && value != "X" {
                queue.append((x, y))
                visited[x][y] = true
                result.append(bfs(x, y, Int(value)!))
                
            }
        }
    }
    
    return result.isEmpty ? [-1] : result.sorted()
}