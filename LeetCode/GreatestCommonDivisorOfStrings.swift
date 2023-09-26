//: [Previous](@previous)

import Foundation
import XCTest

extension String {
    subscript(idx: Int) -> String? {
        
        guard (0..<count).contains(idx) else {
            return nil
        }
        
        let result = index(startIndex, offsetBy: idx)
        return String(self[result])
        
    }
}

class Solution{
    func gcdOfStrings(_ str1: String, _ str2: String) -> String {
//        var longStr = ""
//        var shortStr = ""
//        if str1.count > str2.count {
//            longStr = str1
//            shortStr = str2
//        } else {
//            longStr = str2
//            shortStr = str1
//        }
//
//        let idx = gcd(longStr.count, shortStr.count)
//
//        var result = ""
//        for i in 0..<idx {
//            result += str1[i]!
//        }
//
//        let compareLongStr = String(repeating: result, count: longStr.count / idx)
//        let compareShortStr = String(repeating: result, count: shortStr.count / idx)
//        if compareLongStr == longStr && compareShortStr == shortStr {
//            return result
//        } else { return ""}
        
        guard str1 + str2 == str2 + str1 else { return "" }
        let gcdLength = gcd(max(str1.count, str2.count), min(str1.count, str2.count))
        return String(str1.prefix(gcdLength))
        
    }
    
    private func gcd(_ num1: Int, _ num2: Int) -> Int {
        if num2 == 0 { return num1 }
        return gcd(num2, num1 % num2)
        
    }
}


class Test: XCTestCase {
    func test1Code() {
        let sol = Solution()
        let str = sol.gcdOfStrings("ABCABC", "ABC")
        XCTAssertEqual(str, "ABC")
    }
    func test2Code() {
        let sol = Solution()
        let str = sol.gcdOfStrings("ABABAB", "ABAB")
        XCTAssertEqual(str, "AB")
    }
    
    func test3Code() {
        let sol = Solution()
        let str = sol.gcdOfStrings("LEET", "CODE")
        XCTAssertEqual(str, "")
    }

    func test4Code() {
        let sol = Solution()
        let str = sol.gcdOfStrings("ABCDEF", "ABC")
        XCTAssertEqual(str, "")
    }
    func test5Code() {
        let sol = Solution()
        let str = sol.gcdOfStrings("AAAAAAAAA", "AAADEF")
        XCTAssertEqual(str, "")
    }
    
}

Test.defaultTestSuite.run()


//: [Next](@next)
