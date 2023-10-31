

import Foundation


let input = readLine()!.split(separator: " ").map{ Int($0)! }
let n = input[0]
let m = input[1]

var board: [[Int]] = []
var vis: [[Int]] = .init(
    repeating: .init(repeating: -1, count: m), count: n
)

let dy = [-1, 1, 0, 0]
let dx = [0, 0, -1, 1]

for _ in 1...n {
    let input = readLine()!.map{ Int(String($0))! }
    board.append(input)
    
}

var queue: [(Int, Int)] = []
queue.append((0, 0))
vis[0][0] = 1

while queue.count != 0 {
    
    let cur = queue.removeFirst()
    for dir in 0..<4 {
        let ny = cur.0 + dy[dir]
        let nx = cur.1 + dx[dir]
        
        if ny < 0 || nx < 0 || ny >= n || nx >= m { continue }
        if vis[ny][nx] != -1 { continue }
        if board[ny][nx] == 0 { continue }
        
        queue.append((ny, nx))
        vis[ny][nx] = vis[cur.0][cur.1] + 1
        
    }
    
}
print(vis[n-1][m-1])

