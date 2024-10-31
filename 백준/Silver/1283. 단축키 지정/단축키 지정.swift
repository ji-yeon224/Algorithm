import Foundation

let N = Int(readLine()!)!
var shorts: [String] = []

for _ in 0..<N {
    let word = String(readLine()!)
    print(findShorts(word))
}

func findShorts(_ word: String) -> String {
    var wordList = word.components(separatedBy: " ")
    
    for (index, word) in wordList.enumerated() {
        let firstChar = String(word[word.startIndex]).uppercased()
        if !shorts.contains(firstChar) {
            let charList = word.map { String($0) }
            wordList[index] = makeShortOptionWord(charList, index: 0)
            shorts.append(firstChar)
            return wordList.joined(separator: " ")
        }
    }
    
    for (i, word) in wordList.enumerated() {
        let charList = word.map { String($0) }
        for (j, char) in charList.enumerated() {
            let check = char.uppercased()
            if !shorts.contains(check) {
                wordList[i] = makeShortOptionWord(charList, index: j)
                shorts.append(check)
                return wordList.joined(separator: " ")
            }
        }
    }
    return word
}

func makeShortOptionWord(_ word: [String], index: Int) -> String {
    var newWord = word
    newWord.insert("[", at: index)
    newWord.insert("]", at: index+2)
    return newWord.reduce(""){"\($0)\($1)"}
}