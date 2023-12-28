import Foundation

struct Structure {
    var pillar: Bool
    var roof: Bool
    
}

func solution(_ n:Int, _ build_frame:[[Int]]) -> [[Int]] {
    
    var map: [[Structure]] = Array.init(repeating: Array.init(repeating: Structure(pillar: false, roof: false), count: n+1), count: n+1)
    
    func checkPillar(_ x: Int, _ y: Int) -> Bool {
        if y == 0 || map[y][x].roof || (x>0 && map[y][x-1].roof) || (y > 0 && map[y-1][x].pillar) {
            return true
        } else { return false }
    }
    
    func checkRoof(_ x: Int, _ y: Int) -> Bool {
        if (y > 0 && map[y-1][x].pillar) || (y > 0 && map[y-1][x+1].pillar) || (x > 0 && map[y][x-1].roof && map[y][x+1].roof) {
            return true
        } else { return false }
    }
    
    func structState() -> Bool {
        for y in 0...n {
            for x in 0...n {
                if map[y][x].pillar && !checkPillar(x, y) { return false }
                if map[y][x].roof && !checkRoof(x, y) { return false }
            }
        }
        return true
    }
    
    build_frame.forEach {
        let x = $0[0], y = $0[1], type = $0[2], install = $0[3]
        
        if install == 0 { // 삭제
            if type == 0 {
                map[y][x].pillar = false
                if !structState() {
                    map[y][x].pillar = true
                }
            } else {
                map[y][x].roof = false
                if !structState() {
                    map[y][x].roof = true
                }
            }
            
        } else { // 설치
            if type == 0 {
                if checkPillar(x, y) { map[y][x].pillar = true}
            } else {
                if checkRoof(x, y) { map[y][x].roof = true }
            }
        }
        
    }
    
    var result: [[Int]] = []
    
    for y in 0...n {
        for x in 0...n {
            if map[y][x].pillar { result.append([x, y, 0])}
            if map[y][x].roof { result.append([x, y, 1])}
        }
    }
    
    result = result.sorted {
        
        if $0[0] == $1[0] {
            if $0[1] == $1[1] {
                return $0[2] < $1[2]
            }
            return $0[1] < $1[1]
        }
        
        return $0[0] < $1[0]
    }
    
    return result
}