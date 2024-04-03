import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let M = input[0]
let N = input[1]

typealias Index = (r: Int, c: Int)
var dp: [[Int]] = Array(repeating: Array(repeating: -1, count: N), count: M)
var dir: [Index] = [Index(-1, 0), Index(1, 0), Index(0, -1), Index(0, 1)]

var dest = Index(M-1, N-1)

var graph: [[Int]] = Array(repeating: [], count: M)
for i in 0..<M {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    graph[i] = input
}


func dfs(_ cur: Index) -> Int {
    if cur == dest {
        return 1
    } else if dp[cur.r][cur.c] == -1 {
        dp[cur.r][cur.c] = 0
        
        dir.forEach { d in
            let nxtR = cur.r + d.r
            let nxtC = cur.c + d.c
            if 0..<M ~= nxtR && 0..<N ~= nxtC {
                if graph[cur.r][cur.c] > graph[nxtR][nxtC] {
                    dp[cur.r][cur.c] += dfs(Index(nxtR, nxtC))
                }
                
            }
        }
    }
    
    return dp[cur.r][cur.c]
}

print(dfs(Index(0, 0)))

