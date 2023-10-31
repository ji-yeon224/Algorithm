import Foundation

func solution(_ strlist:[String]) -> [Int] {
    var result: [Int] = []
    for str in strlist {
        result.append(str.count)
    }
    
    return result
}