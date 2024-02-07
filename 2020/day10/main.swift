import Foundation

let filePath = "2020/day10/input"
let content = try String(contentsOfFile: filePath)
var adapters = content.split(separator: "\n").compactMap{ Int($0) }.sorted()

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

let allAdapters = [0] + adapters + [highest]
typealias adapterRating = Int
typealias noOfWays = Int
var waysToReach: [adapterRating : noOfWays] = [0:1]

for i in 1..<allAdapters.count {
    let adapter = allAdapters[i]
    waysToReach[adapter] = (1...3).reduce(0)
        { sum, j in sum + (waysToReach[adapter - j] ?? 0)}
}

print("Part 1: \(difference1 * difference3)")
print("Part 2: \(waysToReach[highest]!)")