const INPUT: (i32, i32) = (264360, 746325);

fn main() {
    println!("Part 2: {}", (INPUT.0..=INPUT.1).filter(|x| is_cand(*x)).count()); // 617
}

fn is_cand(i: i32) -> bool {
    let chars: Vec<char> = i.to_string().chars().collect();
    // Change .count() > 1 for Part 1
    chars.windows(2).all(|x| x[0] <= x[1]) &&
        chars.iter().any(|x| chars.iter().filter(|y| x == *y).count() == 2)
}