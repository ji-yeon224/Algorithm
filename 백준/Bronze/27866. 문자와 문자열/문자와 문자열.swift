extension String {
    subscript(idx: Int) -> String? {
        
        guard (0..<count).contains(idx) else {
            return nil
        }
        
        let result = index(startIndex, offsetBy: idx)
        return String(self[result])
        
    }
}

let str = readLine()!
let idx = Int(readLine()!)!
print(str[idx-1]!)