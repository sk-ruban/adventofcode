import Foundation

let filePath = "2020/day04/input"
var validPassports = 0
let requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let batch_file = content.split(separator: "\n\n")

    for passport in batch_file {
        var foundFields = Set<String>()

        let fields = passport.components(separatedBy: CharacterSet.whitespacesAndNewlines)
        for field in fields {
            foundFields.insert(field.components(separatedBy: ":").first!)
        }
        
        if requiredFields.allSatisfy(foundFields.contains) {
            validPassports += 1
        }
    }
} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(validPassports)") // 226