import Foundation

let filePath = "2020/day09/input"
let content = try String(contentsOfFile: filePath)
let data = content.components(separatedBy: "\n").compactMap(Int.init)

let preamble = 25

func findInvalid(from data: [Int], preamble: Int) -> Int {

    var index = preamble

    while index < data.count {
        let slice = Array(data[(index - preamble)...(index - 1)])
        let sum = data[index]
        var isValid = false

        outerLoop: for j in 0..<slice.count {
            for k in (j + 1)..<slice.count {
                if slice[j] + slice[k] == sum {
                    isValid = true
                    break
                }
            }
        }

        if !isValid {
            return sum
        }
        
        index += 1
    }

    fatalError("All sums are possible")
}

let invalid = findInvalid(from: data, preamble: preamble)
var contiguousSet = [Int]()

outerLoop: for j in 0..<data.count {
    innerLoop: for k in (j+1)..<data.count {
        let newSum = data[j...k].reduce(0, +)
        if newSum > invalid {
            break innerLoop
        }
        else if newSum == invalid {
            contiguousSet = Array(data[j...k])
            break outerLoop
        }
    }
}

print("Part 1: \(invalid)") // 88311122
print("Part 2: \(contiguousSet.min()! + contiguousSet.max()!)") // 13549369