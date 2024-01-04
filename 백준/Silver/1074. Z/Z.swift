import Foundation

func solution() -> Int {
    
    typealias Index = (r: Int, c: Int)
    
    let input = readLine()!.components(separatedBy: " ").map { Int("\($0)")!}
    let n: Int = Int(pow(2.0, Float(input[0])))
    let dest: Index = (input[1], input[2])
    
    var result: Int = 0
    func searchArea(n: Int, start: Index, index: Int) {
        if n == 2 { // 2 x 2
            result = index
            if start.r == dest.r {
                if start.c != dest.c {
                    result += 1
                }
            }
            else {
                if start.c == dest.c {
                    result += 2
                } else { result += 3}
            }
            
            return
        }
        var idx = index
        let midR = (n / 2) + start.r
        let midC = (n / 2) + start.c
        
        let nextR = dest.r < midR ? start.r : midR
        let nextC = dest.c < midC ? start.c : midC
        
        if nextR < midR {
            idx = index
            if nextC >= midC { idx += ((n/2)*(n/2)) }
        } else {
            
            idx = index + (n * n/2)
            if nextC >= midC {
                idx += ((n/2)*(n/2))
            }
        }
        searchArea(n: n / 2, start: (nextR, nextC), index: idx)
        
        
    }
    
    searchArea(n: n, start: (0,0), index: 0)
    
    return result
}

print(solution())
