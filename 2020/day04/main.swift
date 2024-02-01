import Foundation

let filePath = "2020/day04/input"
var part1 = 0
var part2 = 0

struct Passport {
    var byr: String?
    var iyr: String?
    var eyr: String?
    var hgt: String?
    var hcl: String?
    var ecl: String?
    var pid: String?
    var cid: String?

    private func checkValidYear(_ year: String?, _ min: Int, _ max: Int) -> Bool {
        guard let year = year else { return false }
        if Int(year)! >= min && Int(year)! <= max {
            return true
        }
        return false
    }

    private func checkValidHeight(_ height: String?) -> Bool {
        guard let height = height else { return false }
        let unit = String(height.suffix(2))
        guard let value = Int(height.dropLast(2)) else { return false }

        switch unit {
            case "cm": return (150...193).contains(value)
            case "in": return (59...76).contains(value)
            default: return false
        }
    }

    private func checkValidHair(_ color: String?) -> Bool {
        guard let color = color, color.hasPrefix("#") else { return false }
        return color.count == 7 && color.dropFirst().allSatisfy { $0.isHexDigit }
    }

    private func checkValidEye(_ color: String?) -> Bool {
        let validColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return validColors.contains(color ?? "")
    }

    private func checkValidPID(_ pid: String?) -> Bool {
        guard let pid = pid else  {return false }
        return pid.count == 9 && pid.allSatisfy { $0.isNumber }
    }

    var isValid1: Bool {
        return  byr != nil && 
                iyr != nil && 
                eyr != nil && 
                hgt != nil && 
                hcl != nil && 
                ecl != nil && 
                pid != nil
    }

    var isValid2: Bool {
        return  checkValidYear(byr, 1920, 2002) &&
                checkValidYear(iyr, 2010, 2020) &&
                checkValidYear(eyr, 2020, 2030) &&
                checkValidHeight(hgt) &&
                checkValidHair(hcl) &&
                checkValidEye(ecl) &&
                checkValidPID(pid)
    }

    init (from passport: String) {
        let fields = passport.components(separatedBy: CharacterSet.whitespacesAndNewlines)
        for field in fields {
            let components = field.components(separatedBy: ":")
            if components.count == 2 {
                let key = components[0]
                let value = components[1]

                switch key {
                    case "byr": self.byr = value
                    case "iyr": self.iyr = value
                    case "eyr": self.eyr = value
                    case "hgt": self.hgt = value
                    case "hcl": self.hcl = value
                    case "ecl": self.ecl = value
                    case "pid": self.pid = value
                    case "cid": self.cid = value
                    default: break
                }
            }
        }
    }
}

do {
    let content = try String(contentsOfFile: filePath, encoding: .utf8)
    let batch_file = content.components(separatedBy: "\n\n")

    let passports = batch_file.map { Passport(from: $0) }
    part1 = passports.filter { $0.isValid1 }.count
    part2 = passports.filter { $0.isValid2 }.count

} catch {
    print("Could not read the file: \(error)")
}

print("Part 1: \(part1)") // 226
print("Part 2: \(part2)") // 160