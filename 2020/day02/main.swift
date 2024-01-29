import Foundation

let filePath = "2020/day02/input"
var part1 = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let database = content.split(separator: "\n")

    for line in database {
        let parts = line.split(separator: " ").map(String.init)
        let range = parts[0].split(separator: "-").map{ Int($0)! }
        let letter = parts[1].first!
        let password = parts[2]

        var frequencyMap: [Character: Int] = [:]
        for char in password {
            frequencyMap[char, default: 0] += 1
        }

        if let frequency = frequencyMap[letter], frequency >= range[0] && frequency <= range[1] {
            part1 += 1
        }
    }
    
} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(part1)") // 614