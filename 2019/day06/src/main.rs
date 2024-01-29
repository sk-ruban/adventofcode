use std::collections::{HashMap, HashSet};

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

    let mut from_start= HashSet::new();
    let mut start = "YOU";
    while let Some(direct_parent) = orbits.get(start) {
        start = direct_parent;
        from_start.insert(start);
    }

    let mut to_end = HashSet::new();
    let mut end = "SAN";
    while let Some(direct_parent) = orbits.get(end) {
        end = direct_parent;
        to_end.insert(end);
    }

    let journey1 = from_start.difference(&to_end);
    let journey2 = to_end.difference(&from_start);

    println!("Part 1: {}", count); // 227612
    println!("Part 2: {}", journey1.count() + journey2.count()); // 454
}
