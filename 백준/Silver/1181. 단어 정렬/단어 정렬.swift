import Foundation


let count = Int(readLine()!)!
var wordSet: Set<String> = []
for _ in 0..<count {
    wordSet.insert(readLine()!)
}

var wordDict = Dictionary<Int, Array<String>>()

wordSet.forEach { word in
    if wordDict[word.count] == nil {
        wordDict[word.count] = [word]
    } else {
        wordDict[word.count]?.append(word)
    }
    
}
let keySet = wordDict.keys.sorted()
keySet.forEach { key in
    let values = wordDict[key]?.sorted()
    values!.forEach {
        print($0)
    }
}