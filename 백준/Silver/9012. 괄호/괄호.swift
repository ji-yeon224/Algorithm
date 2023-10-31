let count = Int(readLine()!)!
var input: [String] = []

for _ in 0..<count {
    input.append(readLine()!)
}

for element in input {
    checkVPS(element) ? print("YES") : print("NO")
}

func checkVPS(_ ps: String) -> Bool{
    var stack: [Character] = []
    for i in ps {
        if i == "(" {
            stack.append(i)
            continue
        } else {
            if stack.isEmpty {
                return false
            }
            let _ = stack.popLast()
        }
    }

    return stack.isEmpty ? true : false
    
}