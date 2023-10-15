class Solution {
    func increasingTriplet(_ nums: [Int]) -> Bool {
        
        var first = Int.max
        var second = Int.max
        // for i in nums {
        //     if i < first {
        //         first = i
        //     } else if i < second {
        //         second = i
        //     } else if i > second {
        //         return true
        //     }
        // }
        
        return nums.contains { i in
            if i < first {
                first = i
            } else if i < second {
                second = i
            } else if i > second {
                return true
            }
            return false
        }
        
        
        return false
    }
}


class Test: XCTestCase {
    func test1Code() {
        let sol = Solution()
        let str = sol.increasingTriplet([1, 2, 3, 4, 5])
        XCTAssertEqual(str, true)
    }
    
    func test2Code() {
        let sol = Solution()
        let str = sol.increasingTriplet([5, 4, 3, 2, 1])
        XCTAssertEqual(str, false)
    }
    
    func test3Code() {
        let sol = Solution()
        let str = sol.increasingTriplet([2, 1, 5, 0, 4, 6])
        XCTAssertEqual(str, true)
    }
}

Test.defaultTestSuite.run()
