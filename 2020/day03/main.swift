import Foundation

extension StringProtocol {
    subscript(_ index: Int) -> Character? {
        guard index >= 0, index < self.count else {
            return nil
        }

        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

let filePath = "2020/day03/input"
var pos = 0
var part1 = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let database = content.split(separator: "\n")

    for line in database {
        let mod_pos = pos % line.count

        if line[mod_pos] == "#" {
            part1 += 1
        }
        pos += 3
    }
    
} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(part1)") // 220