use std::collections::{HashMap, HashSet};

const INPUT: &str = include_str!("input");

fn main() {
    let paths: Vec<&str> = INPUT.lines().collect();
    let path1 = trace(paths[0]);
    let path2 = trace(paths[1]);

    let intersect = convert(path1.clone())
        .intersection(&convert(path2.clone()))
        .map(|x| x.0.abs() + x.1.abs())
        .min();

    let fewest_steps = path1
        .iter()
        .filter_map(|(k, v)| path2.get(k).map(|x| x + v))
        .min();

    println!("Part 1: {}", intersect.unwrap()); // 266
    println!("Part 2: {}", fewest_steps.unwrap()); // 19242
}

fn trace(path: &str) -> HashMap<(i32, i32), usize> {
    let mut pos = (0,0);
    let mut wire = HashMap::new();
    let mut steps = 0;

    for each in path.split(",") {
        let (dir, dist) = each.split_at(1);
        for _ in 0..dist.parse().unwrap() {
            match dir {
                "U" => pos.1 += 1,
                "D" => pos.1 -= 1,
                "L" => pos.0 -= 1,
                "R" => pos.0 += 1,
                _ => panic!("Wrong direction provided: {}", dir)
            }
            steps += 1;
            wire.insert(pos, steps);
        }
    }
    wire
}

fn convert(map: HashMap<(i32, i32), usize>) -> HashSet<(i32, i32)> {
    map
        .into_iter()
        .map(|(k, _v)| k)
        .collect()
}