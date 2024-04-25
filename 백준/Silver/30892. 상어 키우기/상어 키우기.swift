struct Stack<T> {
    var stack: [T] = []
  
    var count : Int {
        return stack.count
    }
    var isEmpty : Bool {
        return stack.isEmpty
    }
    
    mutating func pop() -> T? {
        return stack.popLast()
    }
    mutating func push(_ element: T) {
        stack.append(element)
    }
    func top() -> T? {
        return stack.last
    }
}

let firstLine = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = firstLine[0]
let K = firstLine[1]
var T = firstLine[2]
let secondLine = readLine()!.split(separator: " ").map{ Int(String($0))! }
var sharks = secondLine.sorted(by:>)
var stack = Stack<Int>()

for _ in 0..<K {
    while !sharks.isEmpty {

        if sharks.last! < T {
            stack.push(sharks.popLast()!)
        }
        else { break }
        
    }
    if stack.isEmpty {
        break
    } else {
        T += stack.pop()!
        
    }
    
}

print(T)
    