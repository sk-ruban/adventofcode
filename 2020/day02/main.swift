import Foundation

let filePath = "2020/day02/input"
var count1 = 0
var count2 = 0

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let database = content.split(separator: "\n")

    for line in database {
        let parts = line.split(separator: " ").map(String.init)
        let range = parts[0].split(separator: "-").map{ Int($0)! }
        let letter = parts[1].first!
        let password = parts[2]

        part1(range: range, letter: letter, password: password)
        part2(range: range, letter: letter, password: password)
    }
    
} catch {
    print("Could not read the file: \(error)")
}

func part1(range: [Int], letter: Character, password: String){
    var frequencyMap: [Character: Int] = [:]
    for char in password {
        frequencyMap[char, default: 0] += 1
    }

    if let frequency = frequencyMap[letter], frequency >= range[0] && frequency <= range[1] {
        count1 += 1
    }
}

func part2(range: [Int], letter: Character, password: String){
    if (password[range[0] - 1]! == letter) != (password[range[1] - 1]! == letter) {
        count2 += 1
    }
}

extension String {
    subscript(_ index: Int) -> Character? {
        guard index >= 0, index < self.count else {
            return nil
        }

        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

print("Part 1: \(count1)") // 614
print("Part 2: \(count2)") // 354