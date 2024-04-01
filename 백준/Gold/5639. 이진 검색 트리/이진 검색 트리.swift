var preNode: [Int] = []
    
while let node = readLine(), let n = Int(node) {
    preNode.append(n)
}

func postOrder(_ root: Int, _ end: Int) {

    if root > end { return }
    let rootNode = preNode[root]
    var rightIdx = end + 1
    
    for i in root+1..<end+1 {
        if rootNode < preNode[i] {
            rightIdx = i
            break
        }
    }
    postOrder(root+1, rightIdx-1)
    postOrder(rightIdx, end)
    print(rootNode)
}

postOrder(0, preNode.count-1)