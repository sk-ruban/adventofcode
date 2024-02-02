import Foundation

let filePath = "2020/day06/input"
let content = try String(contentsOfFile: filePath, encoding: .utf8)
let list = content.split(separator: "\n\n")

var part1 = 0
var part2 = 0

for group in list {
    var anyone_yes = Set<Character>()
    var everyone_yes: [Character: Int] = [:]
    var people = 0

    for person in group.split(separator: "\n") {
        for answer in person {
            anyone_yes.insert(answer)
            everyone_yes[answer, default: 0] += 1
        }
        people += 1
    }
    part1 += anyone_yes.count
    part2 += everyone_yes.filter { $0.value == people }.count
}

print("Part 1: \(part1)") // 6911
print("Part 2: \(part2)") // 3473