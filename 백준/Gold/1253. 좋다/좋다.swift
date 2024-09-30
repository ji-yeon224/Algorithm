let N = Int(readLine()!)!
var numArr = readLine()!.split(separator: " ").map { Int($0)! }
numArr.sort()
var total = 0

for i in 0..<N {
    let tmp = Array(numArr[..<i]) + Array(numArr[(i+1)...])
    var left = 0
    var right = tmp.count-1
    let dest = numArr[i]
    while left < right {
        let tmpSum = tmp[left]+tmp[right]
        if tmpSum == dest {
            total += 1
            break
        } 
        if tmpSum < dest {
            left += 1
            continue
        }
        if tmpSum > dest {
            right -= 1
            continue
        }
    }
}
print(total)