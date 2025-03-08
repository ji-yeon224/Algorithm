import Foundation

var dict = [Int: [Int]]()
var visited = [Bool]()
func bfs(_ start: Int) {
    var queue: [Int] = [start]
    while !queue.isEmpty {
        let cur = queue.removeFirst()
        visited[cur] = true
        for nxt in dict[cur]! {
            if !visited[nxt] {
                visited[nxt] = true
                queue.append(nxt)
            }
        }
    }
}

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var network = 0
    dict = Dictionary(uniqueKeysWithValues: (0..<n).map { ($0, [Int]())})
    visited = Array(repeating: false, count: n)
    
    for i in 0..<n {
        for j in 0..<n {
            if i == j { continue }
            if computers[i][j] == 1 {
                dict[i]?.append(j)    
            }
        }
    }
    for i in 0..<n {
        if !visited[i] {
            bfs(i)
            network += 1
        }
    }

    return network
}