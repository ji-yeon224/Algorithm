
let firstLine = readLine()!.split(separator: " ").map{ Int64(String($0))! }
var secondLine = readLine()!.split(separator: " ").map{ Int64(String($0))! }.sorted(by:>)
var eatableCnt = firstLine[1]
var currentSize: Int64 = firstLine[2]

var stack: [Int64] = []
var cnt = 0

while cnt < eatableCnt {
    while !secondLine.isEmpty {
        if secondLine.last! < currentSize {
            stack.append(secondLine.popLast()!)
        } else {
            break
        }
    }

    
    if stack.isEmpty { 
        break
    } else {
        currentSize += stack.popLast()!

    }
    cnt += 1
}



print(currentSize)       
  