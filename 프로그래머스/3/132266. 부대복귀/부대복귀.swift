import Foundation

func solution(_ n:Int, _ roads:[[Int]], _ sources:[Int], _ destination:Int) -> [Int] {
    
    var graph: [Int: [Int]] = [:]
    roads.forEach {
        graph[$0[0], default: []].append($0[1])
        graph[$0[1], default: []].append($0[0])
    }
    var dist = bfs(graph, destination, n)

    return sources.map { dist[$0] }
}

func bfs(_ graph: [Int: [Int]], _ start: Int, _ n: Int) -> [Int] {
    
    var queue: [Int] = []
    queue.append(start)
    var dist = Array(repeating: -1, count: n+1)
    dist[start] = 0
    while !queue.isEmpty {
        var cur = queue.removeFirst()
        for nxt in graph[cur]! {
            if dist[nxt] != -1 { continue }
            dist[nxt] = dist[cur]+1
            queue.append(nxt)
        }
    }
    return dist
}




