import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var players: [String] = players
    
    var playerMap: [String: Int] = [:]
    for i in 0...players.count - 1 {
        playerMap[players[i]] = i
    }
    
    for call in callings {
        
        var rank = playerMap[call]!
        var frontPlayer = players[rank-1]
        players[rank-1] = players[rank]
        players[rank] = frontPlayer
        
        playerMap[call]! -= 1
        playerMap[frontPlayer]! += 1
        
    }
    
    return players
}

