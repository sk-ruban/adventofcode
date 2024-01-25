use std::fs;

fn main() {
    let input = fs::read_to_string("src/input")
        .expect("File cannot be read");

    let mut part1 = 0;
    let mut part2 = 0;

    for mass in input.lines() {
        let mut fuel = compute_fuel(mass.parse().unwrap());
        part1 += fuel;

        while fuel > 0 {
            part2 += fuel;
            fuel = compute_fuel(fuel);
        }
    }

    println!("{}", part1); // 3337766
    println!("{}", part2); // 5003788
}

fn compute_fuel(mass: i32) -> i32 {
    mass / 3 - 2
}