import Foundation

let dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
var moveArray: [[Int]] = []
var queue: [(Int, Int)] = []
var rowLen = 0
var colLen = 0
var max = Int.max

func solution(_ board:[String]) -> Int {
    var startP: (Int, Int) = (0,0)
    var goalP: (Int, Int) = (0,0)
    
    moveArray = Array.init(repeating: Array.init(repeating: Int.max, count: board[0].count), count: board.count)

    
    for (row, arr) in board.enumerated() {
        for (col, value) in Array(arr).enumerated() {
            if value == "D" {
                moveArray[row][col] = -1
            } else if value == "R" {
                moveArray[row][col] = 0
                startP = (row, col)
            } else if value == "G" {
                goalP = (row, col)
            }
        }
    }
    
    queue = [startP]
    rowLen = moveArray.count
    colLen = moveArray[0].count
    
    while !queue.isEmpty {
        
        let curP = queue.removeFirst()
        if curP == goalP {
            return moveArray[curP.0][curP.1]
        }
        let nextList = movePoint(curP)
        nextList.forEach { dir in
            if moveArray[curP.0][curP.1] + 1 < moveArray[dir.0][dir.1] {
                moveArray[dir.0][dir.1] = moveArray[curP.0][curP.1] + 1
                queue.append(dir)
            }
            
            
        }
        
        
    }
    
    
    
    return -1
}

func movePoint(_ curP: (Int, Int)) -> [(Int, Int)]{
    var result: [(Int, Int)] = []
    dir.forEach { idx in
        var fin = curP
        var nxt = (idx.0 + curP.0, idx.1 + curP.1)
        while (nxt.0 >= 0 && nxt.1 >= 0 && nxt.0 < rowLen && nxt.1 < colLen && moveArray[nxt.0][nxt.1] != -1) {
            fin = nxt
            nxt = (nxt.0 + idx.0, nxt.1 + idx.1)
        }
        
        if fin != curP {
            result.append(fin)
        }
        
    }
    
    return result
}