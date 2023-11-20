import Foundation

var visited: [Bool] = Array(repeating: false, count: 50)

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
        
        if !words.contains(target) {
            return 0
        }
        return dfs(target: target, cur: begin, cnt: 0, words)
         
    }


    func dfs(target: String, cur: String, cnt: Int, _ words: [String]) -> Int {
        
        var minCount = words.count
        
        var count = cnt
        if cur == target {
            return count
        }
        
        for i in 0..<words.count {
            if !visited[i] && checkWord(cur: cur, compare: words[i]) {
                count += 1
                visited[i] = true
                minCount = min(dfs(target: target, cur: words[i], cnt: count, words), minCount)
                visited[i] = false
                count -= 1
            }
        }
        
        return minCount
    }

    func checkWord(cur: String, compare: String) -> Bool {
        
        var count = 0
        
        for i in 0..<cur.count {
            var curIdx = cur.index(cur.startIndex, offsetBy: i)
            var compareIdx = compare.index(compare.startIndex, offsetBy: i)
            if cur[curIdx] == compare[compareIdx] {
                count += 1
            }
        }
        
        
        return count == cur.count - 1 ? true : false
    }