import Foundation
func solution(_ plans:[[String]]) -> [String] {
    
    var result: Array<String> = []
    var stack: [(String, Int)] = []
    var curTime: Int = 0
    
    var plans = plans.map {
        return ($0[0], convertToMinute($0[1]), Int($0[2])!)
    }.sorted {
        $0.1 < $1.1
    }
    
    for (index, value) in plans.enumerated() {
        let curAssign = value
        curTime = curAssign.1
        if index+1 < plans.count {
            let nextAssign = plans[index+1]
            if nextAssign.1 - curAssign.1 < curAssign.2 { // 뒷 순서 과제 시작 시간보다 더 걸릴 때
                stack.append((curAssign.0, curAssign.2 - (nextAssign.1 - curAssign.1)))
            } else { // 과제 완료
                result.append(curAssign.0)
                curTime = curAssign.1 + curAssign.2 // 과제 완료 시간
                var enableTime = nextAssign.1 - curTime // 다음 계획까지 남는 시간
                while enableTime > 0 && !stack.isEmpty { // 다음 과제까지 시간이 남는다면
                    let continueTask = stack.removeLast() // 중단했던 최근 작업 꺼내기
                    if enableTime < continueTask.1 { // 중단 작업이 더 오래 걸리면..
                        stack.append((continueTask.0, continueTask.1-enableTime))
                        break
                    } else {
                        result.append(continueTask.0)
                        enableTime -= continueTask.1
                    }
                    
                }
                
            }
            
        } else { // 마지막 순서 작업
            let (name, start, time) = curAssign
            result.append(name)
            curTime = start + time
        }
        
            
    }
    
    while !stack.isEmpty {
        result.append(stack.removeLast().0)
    }
    
        
    return result
}

private func convertToMinute(_ time: String) -> Int {
    let t = time.components(separatedBy: ":")
    return Int(t[0])!*60 + Int(t[1])!
}