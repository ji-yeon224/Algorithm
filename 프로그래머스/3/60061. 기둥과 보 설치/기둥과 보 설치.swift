import Foundation

struct Structure {
    var pillar: Bool = false
    var board: Bool = false
}

var board: [[Structure]] = []
var size: Int = -1
func solution(_ n:Int, _ build_frame:[[Int]]) -> [[Int]] {
    board = Array(
        repeating: Array(repeating: Structure(), count: n+1), 
        count: n+1
    )
    size = n
    for build in build_frame {
        let x = build[0]
        let y = build[1]
        let a = build[2]
        let b = build[3]
        if b == 1 { 
            if a == 0 {
                board[x][y].pillar = buildPillar(x: x, y: y)
            } else {
                board[x][y].board = buildBoard(x: x, y: y)
            }
        } else {
            if a == 0 {
                deletePillar(x: x, y: y)
            } else {
                deleteBoard(x: x, y: y)
            }
        }
    }
    return makeResult()
}

func isInRange(x: Int, y: Int) -> Bool {
    if 0 <= x && x <= size && 0 <= y && y <= size {
        return true
    } else {
        return false
    }
}

func makeResult() -> [[Int]] {
    var result: [[Int]] = []
    for x in 0...size {
        for y in 0...size {
            if board[x][y].pillar {
                result.append([x, y, 0])
            }
            if board[x][y].board {
                result.append([x, y, 1])
            }
        }
    }
    return result
}

func checkPillar(x: Int, y: Int) -> Bool {
    if isInRange(x: x, y: y) && board[x][y].pillar {
        return true
    }
    return false
}

func checkBoard(x: Int, y: Int) -> Bool {
    if isInRange(x: x, y: y) && board[x][y].board {
        return true
    }
    return false
}

func buildPillar(x: Int, y: Int) -> Bool {
    if y == 0 { 
        return true
    } else if checkPillar(x: x, y: y-1) || checkBoard(x: x-1, y: y) || checkBoard(x: x, y: y) {
        return true
    } else {
        return false
    }
}


func buildBoard(x: Int, y: Int) -> Bool {
    if checkPillar(x: x, y: y-1) || checkPillar(x: x+1, y: y-1) {
        return true
    } else if checkBoard(x: x-1, y: y) && checkBoard(x: x+1, y: y) {
        return true
    } else {
        return false
    }
}

func deletePillar(x: Int, y: Int) {
    board[x][y].pillar = false
    if checkBoard(x: x-1, y: y+1) && !buildBoard(x: x-1, y: y+1){
        board[x][y].pillar = true
    }
    else if checkBoard(x: x, y: y+1) && !buildBoard(x: x, y: y+1) {
       board[x][y].pillar = true
    }
    else if checkPillar(x: x, y: y+1) && !buildPillar(x: x, y: y+1) {
        board[x][y].pillar = true
    }
}

func deleteBoard(x: Int, y: Int) {
    board[x][y].board = false
    if checkBoard(x: x+1, y: y) && !buildBoard(x: x+1, y: y) {
        board[x][y].board = true
    }
    else if checkBoard(x: x-1, y: y) && !buildBoard(x: x-1, y: y) {
        board[x][y].board = true
    }
    else if checkPillar(x: x+1, y: y) && !buildPillar(x: x+1, y: y) {
        board[x][y].board = true
    } else if checkPillar(x: x, y: y) && !buildPillar(x: x, y: y) {
        board[x][y].board = true
    }
}

