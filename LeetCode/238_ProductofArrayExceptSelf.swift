//: [Previous](@previous)

import Foundation
import XCTest

class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        
        var num = 1
        var numRev = 1
        return nums.map {
            var tmp = num
            num *= $0
            return tmp
        }.enumerated().reversed()
            .map {
                var tmp = $1 * numRev
                numRev *= nums[$0]
                return tmp
            }
            .reversed()
    }
}

/*
 1 2 3 4 // 원본
 1 2 6 24
 1 1 2 6 // 첫번째 map
 0,1 1,1 2,2, 3,6
 6 2 1 1 // rev
 4 3 2 1 // 원본 rev
 6 8 12 24
 
 
 
 */


class Test: XCTestCase {
    func test1Code() {
        let sol = Solution()
        let str = sol.productExceptSelf([1, 2, 3, 4])
        XCTAssertEqual(str, [24, 12, 8, 6])
    }
    
    func test2Code() {
        let sol = Solution()
        let str = sol.productExceptSelf([-1, 1, 0, -3, 3])
        XCTAssertEqual(str, [0, 0, 9, 0, 0])
    }

   
    
}

Test.defaultTestSuite.run()


//: [Next](@next)
