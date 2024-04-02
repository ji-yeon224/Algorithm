import Foundation

var sudoku: [[Int]] = []
var fillComplete = false
for _ in 0..<9 {
    let line = Array(readLine()!).map{Int(String($0))!}
    sudoku.append(line)
}

func fillSudoku(_ idx: Int) {

    if fillComplete {
        return
    }
    
    for i in idx..<81 {
        let row = i / 9
        let col = i % 9
        if sudoku[row][col] == 0 {
            for num in 1...9 {
                if checkNum(row, col, num, sudoku: sudoku) {
                    sudoku[row][col] = num
                    fillSudoku(i+1)
                    
                }
            }
            sudoku[row][col] = 0
            return
        }
    }
    fillComplete = true
    printSudoku()
    
}

func checkNum(_ row: Int, _ col: Int, _ target: Int, sudoku: [[Int]]) -> Bool {
    let squareRow = row / 3 * 3
    let squareCol = col / 3 * 3
    
    for i in 0..<9 {
        if sudoku[i][col] == target { return false }
        if sudoku[row][i] == target { return false }
        let sr = i / 3
        let sc = i % 3
        if sudoku[squareRow+sr][squareCol+sc] == target { return false }
    }
    return true
}

fillSudoku(0)

func printSudoku() {
    for i in 0..<9 {
        print(sudoku[i].map{String($0)}.joined())
    }
}
