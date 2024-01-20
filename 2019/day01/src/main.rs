use std::fs;

fn main() {
    let input = fs::read_to_string("src/input")
        .expect("File cannot be read");
    let mut part1 = 0;
    for line in input.lines() {
        let mass: i32 = line.parse().unwrap();
        part1 += mass / 3 - 2;
    }
    println!("{}", part1); // 3337766
}

