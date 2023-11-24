import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    
    var answer = Array(repeating: -1, count: numbers.count)
    var stack: [(Int, Int)] = []
    
    for (idx, num) in numbers.enumerated() {
        while (!stack.isEmpty) {
            if (stack[stack.count-1].1 < num) {
                answer[stack.removeLast().0] = num
            } else { break }
        }
        stack.append((idx, num))
    }
    return answer
}