let N = Int(readLine()!)!
var numArr: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
numArr.sort()

var answer = 3000000000
var answerList: [Int] = [0, 0, 0]
for i in 0..<N-2 {
    var leftIdx = i+1
    var rightIdx = N-1
    
    while leftIdx < rightIdx {
        let sum = numArr[i] + numArr[leftIdx] + numArr[rightIdx]
        if abs(sum) < answer {
            answer = abs(sum)
            answerList[0] = numArr[i]
            answerList[1] = numArr[leftIdx]
            answerList[2] = numArr[rightIdx]
        }
        if sum < 0 {
            leftIdx += 1
        } else {
            rightIdx -= 1
        }
    }
}
answerList.forEach {
    print($0, terminator: " ")
}