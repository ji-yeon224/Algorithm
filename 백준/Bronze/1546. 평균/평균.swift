let N = Double(String(readLine()!))!
let subjects = String(readLine()!).split(separator: " ").map { Int($0)! }
let M = Double(subjects.max()!)
var answer: Double = 0

subjects.forEach {
    answer += Double($0)/M*100.0
}
print(answer/N)