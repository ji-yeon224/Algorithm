class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        var result = ""
        var i = 0, j = 0
        let word1Arr = Array(word1)
        let word2Arr = Array(word2)

        while i < word1Arr.count || j < word2Arr.count {
            if i < word1Arr.count {
                let char1 = word1Arr[i]
                result += "\(char1)"
            }
            if j < word2Arr.count {
                let char2 = word2Arr[i]
                result += "\(char2)"
            }
            i += 1
            j += 1
        }


        return result
    }

}