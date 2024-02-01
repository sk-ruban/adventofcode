import Foundation

let filePath = "2020/day05/input"

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let passes = content.split(separator: "\n")
    var seats = [Int]()

    for pass in passes {
        var row_max = 128
        var row_min = 0
        var col_max = 8
        var col_min = 0

        for partition in pass {
            switch partition {
                case "F": row_max = (row_max + row_min) / 2
                case "B": row_min = row_min + ((row_max - row_min) / 2)
                case "L": col_max = (col_max + col_min) / 2
                case "R": col_min = col_min + ((col_max - col_min) / 2)
                default: break  
            }
        }
        let seat_id = row_min * 8 + col_min
        seats.append(seat_id)
    }

    let part1 = seats.max()!
    let part2 = (seats.min()!...seats.max()!).filter{ !seats.contains($0) }.first!

    print("Part 1: \(part1)") // 878
    print("Part 2: \(part2)") // 504
}