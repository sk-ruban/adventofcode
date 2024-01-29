use std::collections::HashMap;

const INPUT: &str = include_str!("input");

fn main() {
    let mut orbits: HashMap<String, String> = HashMap::new();

    for line in INPUT.lines() {
        let parent = &line[0..=2];
        let orbiter = &line[4..=6];

        orbits.insert(orbiter.into(), parent.into());
    }

    let mut count = 0;
    for mut child in orbits.keys() {
        while let Some(direct_parent) = orbits.get(child) {
            child = direct_parent;
            count += 1
        }
    }

    println!("Part 1: {}", count) // 227612
}
