import Foundation

func solution(_ tickets:[[String]]) -> [String] {
  
    var visited = Array(repeating: false, count: tickets.count)
    var route: [String] = []
    
    let sortedTickets = tickets.sorted() {
        $0[1] < $1[1]
    }
    
    func dfs(_ start: String) {
        
        if route.count == sortedTickets.count {
            route.append(start)
            return
        }
        
        for i in 0..<sortedTickets.count {
            let ticket = sortedTickets[i]
            if ticket[0] == start && !visited[i] {
                visited[i] = true
                route.append(ticket[0])
                dfs(ticket[1])
                
                if route.count == sortedTickets.count + 1 {
                    return
                }
                
                visited[i] = false
                route.removeLast()
            }
        }
        
    }
    
    dfs("ICN")
    return route
    
}
