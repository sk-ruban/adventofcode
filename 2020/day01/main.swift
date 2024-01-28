import Foundation

let filePath = "2020/day01/input" 
var part1: Int = 0
var part2: Int = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n").map(String.init)

    for a in lines {
        for b in lines {
            let a = Int(a) ?? 0
            let b = Int(b) ?? 0
            if a + b == 2020 {
                part1 = a*b 
            }
            for c in lines {
                let c = Int(c) ?? 0
                if a + b + c == 2020 {
                    part2 = a*b*c
                }
            }
        }
    }
    
} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(part1)") // 1007104
print("Part 2: \(part2)") // 18847752