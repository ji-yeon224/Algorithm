import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    
    var yearningMap = Dictionary(uniqueKeysWithValues: zip(name, yearning))
    return photo.map{ $0.reduce(0) { $0 + (yearningMap[$1] ?? 0) }}
//     var yearningMap: [String: Int] = [:]
//         var result: [Int] = []
        
//         for i in 0..<name.count {
//             yearningMap[name[i]] = yearning[i]
//         }
//         photo.forEach {
//             var sum = 0
//             $0.map { sum += yearningMap[$0] ?? 0}
//             result.append(sum)
            
//         }
        
//         return result
}