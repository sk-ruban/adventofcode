import Foundation

let filePath = "2020/day07/input"
let content = try String(contentsOfFile: filePath, encoding: .utf8)
let rules = content.split(separator: "\n")

typealias inner = String
typealias outer = String
var bagGraph = [inner: [outer]]()

for rule in rules {
    let parts = rule.components(separatedBy: " bags contain ")
    let outerBag = parts[0]
    let innerBags = parts[1].components(separatedBy: ",")

    for bag in innerBags {
        let innerParts = bag.trimmingCharacters(in: .whitespaces).components(separatedBy: " ")
        let count = innerParts[0]
        let innerBag = innerParts[1] + " " + innerParts[2]

        bagGraph[innerBag, default: []].append(outerBag)
    }
}

func findAllContaining(for bag: String, in graph: [inner: [outer]]) -> Set<String> {
    var visited = Set<String>()
    var toVisit = [bag]

    while !toVisit.isEmpty {
        let currentBag = toVisit.removeLast()
        guard let containingBags = graph[currentBag] else {continue}

        for containingBag in containingBags where !visited.contains(containingBag) {
            visited.insert(containingBag)
            toVisit.append(containingBag)
        }
    }

    return visited
}

print("Part 1: \(findAllContaining(for: "shiny gold", in: bagGraph).count)") // 274