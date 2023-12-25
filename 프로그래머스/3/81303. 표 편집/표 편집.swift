import Foundation

class Node {
    var up: Node?
    var down: Node?
    var idx: Int = 0
    init(up: Node?, down: Node?, idx: Int) {
        self.up = up
        self.down = down
        self.idx = idx
    }
}
func solution(_ n:Int, _ k:Int, _ cmd:[String]) -> String {
    
    var result: [String] = Array(repeating: "O", count: n)
    var linkedList: [Node] = []
    for i in 0..<n {
        linkedList.append(Node(up: nil, down: nil, idx: i))
    }
    linkedList[0].down = linkedList[1]
    
    for i in 1..<n-1 {
        linkedList[i].up = linkedList[i-1]
        linkedList[i].down = linkedList[i+1]
    }
    linkedList[n-1].up = linkedList[n-2]
    var cur: Node = linkedList[k]
    var delete: [Node] = []
    
    cmd.forEach {
        let command = $0.components(separatedBy: " ")

        switch command[0] {
        case "U":
            let cnt = Int(command[1])!
            for _ in 0..<cnt {
                cur = cur.up!
            }
        case "D":
            let cnt = Int(command[1])!
            for _ in 0..<cnt {
                cur = cur.down!
            }
        case "C":
            delete.append(cur)
            result[cur.idx] = "X"
            cur.up?.down = cur.down
            cur.down?.up = cur.up
            if cur.down == nil {
                cur = cur.up!
            } else {
                cur = cur.down!
            }
            
        case "Z":
            let popData = delete.removeLast()
            result[popData.idx] = "O"
            popData.up?.down = popData
            popData.down?.up = popData
        default: break
        }
    }
 
    return result.joined()
}
