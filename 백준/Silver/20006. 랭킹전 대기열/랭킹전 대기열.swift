import Foundation

struct Info: Hashable {
    let level: Int
    let name: String
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
let p = input[0]
let m = input[1]

var rooms: [Info:[Info]] = [:]
var keys: [Info] = []

for _ in 0..<p {
    let input = readLine()!.split(separator: " ").map { String($0) }
    let level = Int(input[0])!
    let name = input[1]
    
    let info = Info(level: level, name: name)
    if keys.isEmpty {
        keys.append(info)
        rooms[info] = [info]
    } else {
        var isEnter = false
        for k in keys {
            if abs(k.level - level) <= 10 && rooms[k]!.count < m {
            rooms[k]!.append(info)
            isEnter = true
            break
        }
        }
        if !isEnter {
            keys.append(info)
            rooms[info] = [info]
        }
        
    }
    
}

for k in keys {
    var room = rooms[k]!
    room = room.sorted(by: { $0.name < $1.name })
    print(room.count == m ? "Started!" : "Waiting!")
    for info in room {
        print(info.level, info.name)
    }
}