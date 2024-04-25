

let firstLine = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = firstLine[0]
let K = firstLine[1]
var T = firstLine[2]
let secondLine = readLine()!.split(separator: " ").map{ Int(String($0))! }
var sharks = secondLine.sorted(by:>)
var stack: [Int] = []

for _ in 0..<K {
    while !sharks.isEmpty {

        if sharks.last! < T {
            stack.append(sharks.popLast()!)
        }
        else { break }
        
    }
    if stack.isEmpty {
        break
    } else {
        T += stack.popLast()!
        
    }
    
}

print(T)
    