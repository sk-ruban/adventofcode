import Foundation

let filePath = "2020/day10/input"
let content = try String(contentsOfFile: filePath)
let adapters = content.split(separator: "\n").compactMap{ Int($0) }

let highest = adapters.max()! + 3
var current = 1
var previous = 0
var difference1 = 0
var difference3 = 1

while current != highest {
    if adapters.contains(current) {
        let difference = current - previous
        switch difference {
            case 1: difference1 += 1
            case 3: difference3 += 1
            default: break
        }
        previous = current
    }
    current += 1
}

print("Part 1: \(difference1 * difference3)")