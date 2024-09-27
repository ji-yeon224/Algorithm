let N = Int(readLine()!)!
var rankList = [Int]()

for _ in 0..<N {
    let num = Int(readLine()!)!
    rankList.append(num)
}
rankList.sort()

var complain = 0
for (index, rank) in rankList.enumerated() {
    complain += abs(index+1-rank)
}
print(complain)