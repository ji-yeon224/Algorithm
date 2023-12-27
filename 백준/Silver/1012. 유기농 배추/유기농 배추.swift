
import Foundation

struct Coord {
    var x: Int
    var y: Int
    
}

let cnt = Int(readLine()!)!

for _ in 0..<cnt {
    print(solution())
}


func solution() -> Int {
    let dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
    let m = input[0], n = input[1], k = input[2]
    var cabbage: [[Int]] = Array.init(repeating: Array.init(repeating: 0, count: m), count: n)
    var visited: [[Bool]] = Array.init(repeating: Array.init(repeating: false, count: m), count: n)
    
    for _ in 0..<k {
        let worm = readLine()!.components(separatedBy: " ").map { Int($0)! }
        cabbage[worm[1]][worm[0]] = 1
    }
    var queue: [Coord] = []
    
    func bfs(coord: Coord) {
        queue.append(coord)
        visited[coord.y][coord.x] = true
        
        while !queue.isEmpty {
            let c = queue.removeFirst()
            let x = c.x, y = c.y
            
            for i in 0..<4 {
                let nx = x + dir[i].0
                let ny = y + dir[i].1
                if validCoord(x: nx, y: ny) && cabbage[ny][nx] == 1 && !visited[ny][nx]{
                    visited[ny][nx] = true
                    queue.append(Coord(x: nx, y: ny))
                }
            }
        }
        
    }
    
    func validCoord(x: Int, y: Int) -> Bool {
        return 0..<m ~= x && 0..<n ~= y
    }
    
    
    
    
    
    var result = 0
    for y in 0..<n {
        for x in 0..<m {
            if cabbage[y][x] == 1 && !visited[y][x] {
                result += 1
                bfs(coord: Coord(x: x, y: y))
            }
        }
    }
    
    return result
    
}
