import Foundation

var result: Int = 0
var visited = Array(repeating: false, count: 200)

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    
    for i in 0..<n {
        if(!visited[i]) {
            result += 1
            dfs(computers, i)
        }
    }
    
    return result
}

func dfs(_ computers: [[Int]], _ idx: Int) {
    
    let links = computers[idx]
    visited[idx] = true
    for i in 0..<links.count {
        if i == idx { continue }
        if links[i] == 1 && !visited[i] {
            dfs(computers, i)
           
        }
    }
    
}