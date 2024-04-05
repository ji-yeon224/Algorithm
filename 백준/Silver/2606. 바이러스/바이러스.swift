
struct Queue {
    var queue: [Int] = []
    var index = 0
    
    var isEmpty: Bool {
        return index == queue.count
    }
    mutating func enqueue(_ num: Int) {
        queue.append(num)
    }
    mutating func dequeue() -> Int {
        let num = queue[index]
        index += 1
        return num
    }
}

    

func bfs() -> Int {
    var visited: [Bool] = Array(repeating: false, count: N+1)    
    var queue = Queue()
    queue.enqueue(1)
    visited[1] = true
    
    while !queue.isEmpty {
        let cur = queue.dequeue()
        dict[cur]!.forEach {
            if !visited[$0] {
                queue.enqueue($0)
                visited[$0] = true
                answer += 1
            }
        }
    }
    return answer
}


let N = Int(readLine()!)!
let link = Int(readLine()!)!
var answer = 0

var dict: [Int: [Int]] = [:]
for i in 1...N {
    dict[i] = []
}
for _ in 0..<link {
    let input: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    dict[input[0]]!.append(input[1])
    dict[input[1]]!.append(input[0])
}
print(bfs())

