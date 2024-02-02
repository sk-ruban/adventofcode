import Foundation

let filePath = "2020/day05/input"

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let passes = content.split(separator: "\n")
    var seats = [Int]()

    for pass in passes {
        let rowPart = pass.prefix(7).replacingOccurrences(of: "F", with: "0").replacingOccurrences(of: "B", with: "1")
        let colPart = pass.suffix(3).replacingOccurrences(of: "L", with: "0").replacingOccurrences(of: "R", with: "1")

        if let row = Int(rowPart, radix: 2), let col = Int(colPart, radix: 2) {
            let seatID = row * 8 + col
            seats.append(seatID)
        }
    }

    let part1 = seats.max()!
    let part2 = (seats.min()!...seats.max()!).filter{ !seats.contains($0) }.first!

    print("Part 1: \(part1)") // 878
    print("Part 2: \(part2)") // 504
}