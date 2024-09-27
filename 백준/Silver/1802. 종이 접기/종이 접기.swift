let T = Int(readLine()!)!
for _ in 0..<T {
    solution()
}
func solution() {
    let paper = readLine()!.compactMap { $0.wholeNumberValue }
    if paper.count < 3 {
        print("YES")
    } else {
        let answer = divide(paper) ? "YES" : "NO"
        print(answer)
    }
    
}

func divide(_ arr: [Int]) -> Bool {
    if arr.count == 1 {
        return true
    }
    
    let mid = arr.count / 2
    let left = Array(arr[0..<mid])
    let right = arr[mid+1..<arr.count].map { 1-$0 }
    let revRight = Array(right.reversed())
    
    if left != revRight {
        return false
    } 
    
    return divide(left)
}