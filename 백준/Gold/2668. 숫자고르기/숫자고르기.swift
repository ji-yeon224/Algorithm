import Foundation

let N = Int(readLine()!)!
var numDict: [Int:Int] = [:]
for i in 1...N {
    numDict[i] = Int(readLine()!)!
}

var visited: [Bool] = Array(repeating: false, count: N+1)
var results: [Int] = []

for i in 1...N {
    if !results.contains(i) {
        var visitList = [i]
        dfs(node: i, visitList: &visitList)
        visited = Array(repeating: false, count: N+1)
    }
}

print(results.count)
results.sort()
results.forEach { print($0) }

func dfs(node: Int,  visitList: inout [Int]) {
    visited[node] = true
    let nextNode = numDict[node]!
    if visited[nextNode] { // 이미 방문
        if visitList.first == nextNode {
            results.append(contentsOf: visitList)
        }
    } else {
        visitList.append(nextNode)
        dfs(node: nextNode, visitList: &visitList)
    }
}
