import Foundation

let filePath = "2020/day08/input"
let content = try String(contentsOfFile: filePath)
let program = content.split(separator: "\n").map {
    let parts = $0.components(separatedBy: " ")
    return (String(parts[0]), Int(parts[1])!)
}

func execute(_ program: [(String, Int)]) -> (Bool, Int) {
    var prev_inst = Set<Int>()
    var line = 0
    var accumulator = 0

    while !prev_inst.contains(line) {
        if line == program.count {
            return (true, accumulator)
        }

        prev_inst.insert(line)
        let (op, arg) = program[line]

        switch op {
            case "acc": 
                accumulator += arg
                line += 1
            case "jmp": 
                line += arg
            case "nop": 
                line += 1
            default: print("Invalid operation!") 
        }
    }

    return (false, accumulator)
}

func updateProgram(_ program:[(String, Int)]) -> Int {
    for line in program.indices {
        var newProgram = program
        let (op, arg) = newProgram[line]

        if op == "jmp" || op == "nop" {
            newProgram[line] = (op == "jmp" ? "nop" : "jmp", arg)

            let (terminated, accumulator) = execute(newProgram)
            if terminated {
                return accumulator
            }
        }
    }

    fatalError("No solution found")
}

print("Part 1: \(execute(program).1)") // 1816
print("Part 2: \(updateProgram(program))") // 1149