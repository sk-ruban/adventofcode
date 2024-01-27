fn main() {
    let mut counter = 0;
    for i in 264360..=746325 {
        if adjacent_digit(i) & never_decrease(i) {
            counter += 1;
        }
    }
    println!("Part 1: {}", counter)
}

fn to_digit_vec(num: usize) -> Vec<usize> {
    num
        .to_string()
        .chars()
        .filter_map(|x| x.to_digit(10))
        .map(|x| x as usize)
        .collect()
}

fn adjacent_digit(num: usize) -> bool {
    let mut first_digit: usize = 0;
    for each in to_digit_vec(num) {
        if each == first_digit {
            return true
        }
        first_digit = each;
    }
    return false
}

fn never_decrease(num: usize) -> bool {
    let mut first_digit: usize = 0;
    for each in to_digit_vec(num) {
        if each < first_digit {
            return false
        }
        first_digit = each;
    }
    return true
}

