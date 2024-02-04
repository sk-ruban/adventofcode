import Foundation

let filePath = "2020/day07/input"
let content = try String(contentsOfFile: filePath, encoding: .utf8)
let rules = content.split(separator: "\n")

typealias inner = String
typealias outer = String
var bagGraph1 = [inner: [outer]]()
var bagGraph2 = [outer: [inner: Int]]()

for rule in rules {
    let parts = rule.components(separatedBy: " bags contain ")
    let outerBag = parts[0]
    let innerBags = parts[1].components(separatedBy: ",")

    if !innerBags[0].starts(with: "no other") {
        for bag in innerBags {
            let innerParts = bag.trimmingCharacters(in: .whitespaces).components(separatedBy: " ")
            guard let count = Int(innerParts[0]) else {continue}
            let innerBag = innerParts[1] + " " + innerParts[2]

            bagGraph1[innerBag, default: []].append(outerBag)
            bagGraph2[outerBag, default: [:]][innerBag] = count
        }
    }
}

func findAllContaining(for bag: String) -> Set<String> {
    var visited = Set<String>()
    var toVisit = [bag]

    while !toVisit.isEmpty {
        let currentBag = toVisit.removeLast()
        guard let containingBags = bagGraph1[currentBag] else {continue}

        for containingBag in containingBags where !visited.contains(containingBag) {
            visited.insert(containingBag)
            toVisit.append(containingBag)
        }
    }

    return visited
}

func findChildrenCount(in bag: String) -> Int {
    let contents = bagGraph2[bag] ?? [:]
    return 1 + contents.map { $0.value * findChildrenCount(in: $0.key)}.reduce(0, +)
}

print("Part 1: \(findAllContaining(for: "shiny gold").count)") // 274
print("Part 2: \(findChildrenCount(in: "shiny gold") - 1)") // 158730