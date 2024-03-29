let N = Int(String(readLine()!))!
var graph: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: N)
var visited: [Bool] = Array(repeating: false, count: N)
for i in 0..<N {
    graph[i] = readLine()!.split(separator: " ").map { Int(String($0))! }
}
var answer = Int.max
func dfs(_ start: Int, _ cnt: Int ) {
    if cnt == N/2 {
        var team1 = 0
        var team2 = 0
        for i in 0..<N {
            for j in 0..<N {
                if visited[i] && visited[j] {
                    team1 += graph[i][j]
                } else if !visited[i] && !visited[j] {
                    team2 += graph[i][j]
                }
            }
        }
        answer = min(answer, abs(team1-team2))
        return 
    } else {
        for i in start..<N {
            if !visited[i] {
                visited[i] = true
                dfs(i, cnt+1)
                visited[i] = false
            }
        }
    }
}

dfs(0, 0)
print(answer)
