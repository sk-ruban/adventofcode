import Foundation

extension StringProtocol {
    subscript(_ index: Int) -> Character? {
        guard index >= 0, index < self.count else {
            return nil
        }

        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

func steer_slope(_ right: Int, _ down: Int, _ map: [Substring]) -> Int {
    var pos = 0
    var trees_hit = 0

    for y in stride(from: 0, to: map.count, by: down) {
        let x = pos % map[y].count
        if map[y][x] == "#" {
            trees_hit += 1
        }
        pos += right
    }

    return trees_hit
}

let filePath = "2020/day03/input"

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let map = content.split(separator: "\n")

    let part1 = steer_slope(3, 1, map)
    print("Part 1: \(part1)") // 220

    let part2 = steer_slope(1, 1, map) * part1 * steer_slope(5, 1, map) * steer_slope(7, 1, map) * steer_slope(1, 2, map)
    print("Part 2: \(part2)") // 2138320800
    
} catch {
    print("Could not read the file: \(error)")
}