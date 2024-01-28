import Foundation

let filePath = "2020/day01/input" 
var part1: Int = 0
var part2: Int = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let numbers = content.split(separator: "\n").compactMap { Int($0) }

    var seen = Set<Int>()
    for i in numbers {
        let complement = 2020 - i
        if seen.contains(complement) {
            part1 = i * complement
            break
        }
        seen.insert(i)
    }

   outerLoop: for a in numbers {
        for b in numbers {
            for c in numbers {
                if a + b + c == 2020 {
                    part2 = a*b*c
                    break outerLoop
                }
            }
        }
    }
    
} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(part1)") // 1007104
print("Part 2: \(part2)") // 18847752