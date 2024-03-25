import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = true
    
    var stack: [String] = []
    
    for s in Array(s) {
        if s == "(" {
            stack.append("(")
        } else {
            if !stack.isEmpty {
                stack.removeLast()
            } else {
                ans = false
                break
            }
            
        }
    }
    
    if !stack.isEmpty {
        ans = false
    }

    return ans
}