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

print("Part 1: \(findInvalid(from: data, preamble: preamble))") // 88311122