import Foundation

func solution(_ sequence:[Int]) -> Int64 {
    var answer = Int.min
    if sequence.count == 1 {
        return Int64(max(sequence[0], sequence[0] * -1))
    }
    var mdp = Array(repeating: 0, count: sequence.count)
    var pdp = Array(repeating: 0, count: sequence.count)
    var minus: [Int] = [-1]
    var plus: [Int] = [1]
    for i in 1..<sequence.count {
        minus.append(minus[i-1] * -1)
        plus.append(plus[i-1] * -1)
    }
    
    mdp[0] = sequence[0] * -1
    pdp[0] = sequence[0]
    
    for i in 1..<sequence.count {
        let m = sequence[i]*minus[i]
        let p = sequence[i]*plus[i]
        mdp[i] = max(mdp[i-1]+m, m)
        pdp[i] = max(pdp[i-1]+p, p)
        
        answer = max(answer, mdp[i], pdp[i])
    }
    return Int64(answer)
}