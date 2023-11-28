import Foundation

func solution(_ book_time:[[String]]) -> Int {
    
    var reservList: [[Int]] = book_time.map {
        
        let enterTime = $0[0].components(separatedBy: ":").map { Int($0)! }
        let exitTime = $0[1].components(separatedBy: ":").map { Int($0)! }
        return [enterTime[0] * 60 + enterTime[1], exitTime[0] * 60 + exitTime[1] + 10]
        
    }
    
    reservList.sort(by: { $0[0] < $1[0] })
    
    var room: [Int] = []
    for time in reservList {
        if room.isEmpty {
            room.append(time[1])
        } else {
            if time[0] < room.min()! {
                room.append(time[1])
            } else {
                let index = room.firstIndex(where: { $0 == room.min() })!
                room[index] = time[1]
            }
        }
    }
    
    return room.count
}