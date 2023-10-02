class Solution {
    func reverseVowels(_ s: String) -> String {
            
        var result = Array(s)
        var vowels:[Character] = []

        // 모음인 요소들 모아두기
        for i in 0..<result.count {
            if isEqualVowels(result[i]) {
                vowels.append(result[i])
            }
        }
        
        // 모음을 만나면 모음 배열에서 pop()하여 교체
        for i in 0..<result.count {
            if isEqualVowels(result[i]) {
                guard let char = vowels.popLast() else {
                    break
                }
                result[i] = char
            }
        }
        return String(result)
    }
    
    // 모음인지 아닌지 판단하는 함수 
    func isEqualVowels(_ char: Character) -> Bool {
        let c = char.lowercased() // 모음 판단 시 대소문자 구분 안함 
        
        if c == "a" || c == "e" || c == "i" || c == "o" || c == "u" {
            return true
        }
        else {
            return false
        }
    }
}