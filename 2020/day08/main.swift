import Foundation

let filePath = "2020/day08/input"
let content = try String(contentsOfFile: filePath, encoding: .utf8)
let program = content.split(separator: "\n")

var prev_inst = Set<Int>()
var line = 0
var accumulator = 0
var jumps = 0

while !prev_inst.contains(line) {
    prev_inst.insert(line)
    let contents = program[line].components(separatedBy: " ")
    let op = contents[0]
    let arg = Int(contents[1])!

    switch op {
        case "acc": 
            accumulator += Int(arg)
            line += 1
        case "jmp": 
            line += Int(arg)
        case "nop": 
            line += 1
        default: print("Invalid argument!") 
    }
}

print("Part 1: \(accumulator)") // 1816