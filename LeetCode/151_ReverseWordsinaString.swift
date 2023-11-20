class Solution {
    func reverseWords(_ s: String) -> String {
        var str = s.split(separator: " ")
        str.reverse()
        var result = ""
        for s in str {
            result.append(String(s))
            result.append(" ")
        }
        return result.trimmingCharacters(in: .whitespaces)
    }
}

class Test: XCTestCase {
    func test1Code() {
        let sol = Solution()
        let str = sol.reverseWords("the sky is blue")
        XCTAssertEqual(str, "blue is sky the")
    }

    func test2Code() {
        let sol = Solution()
        let str = sol.reverseWords("  hello world  ")
        XCTAssertEqual(str, "world hello")
    }
    
    func test3Code() {
        let sol = Solution()
        let str = sol.reverseWords("a good   example")
        XCTAssertEqual(str, "example good a")
    }
   
    
}

Test.defaultTestSuite.run()