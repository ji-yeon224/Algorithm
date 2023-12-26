import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    
    let sortData = data.sorted{$0[0] > $1[0]}.sorted { $0[col-1] < $1[col-1] }
    var modSumList: [Int] = []
    for i in row_begin-1..<row_end {
        modSumList.append(sortData[i].reduce(0) { 
            $0 + $1%(i+1)
        })
    }
   
    return modSumList.reduce(0, ^)
}