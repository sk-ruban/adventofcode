use std::collections::HashSet;

const INPUT: &str = include_str!("input");

fn main() {
    let paths: Vec<&str> = INPUT.lines().collect();
    let path1 = trace(paths[0]);
    let path2 = trace(paths[1]);

    let intersect = path1
        .intersection(&path2)
        .map(|x| x.0.abs() + x.1.abs())
        .min();

    println!("Part 1: {:?}", intersect); // 266
}

fn trace(path: &str) -> HashSet<(i32, i32)> {
    let mut pos = (0,0);
    let mut wire = HashSet::new();

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
            wire.insert(pos);
        }
    }
    wire
}