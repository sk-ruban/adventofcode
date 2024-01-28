import Foundation

let filePath = "2020/day01/input" 

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let lines = content.split(separator: "\n").map(String.init)

    for a in lines {
        for b in lines {
            let a = Int(a) ?? 0
            let b = Int(b) ?? 0
            if a + b == 2020 {
                print("Part 1: \(a) * \(b) = \(a*b)") // 1007104
            }
        }
    }
    
} catch {
    print("Could not read the file: \(error)")
}