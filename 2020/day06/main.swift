import Foundation

let filePath = "2020/day06/input"
let content = try String(contentsOfFile: filePath, encoding: .utf8)
let list = content.split(separator: "\n\n")

var part1 = 0

for group in list {
    var yes = Set<Character>()
    for person in group.split(separator: "\n") {
        for answer in person {
            yes.insert(answer)
        }
    }
    part1 += yes.count
}

print("Part 1: \(part1)")
