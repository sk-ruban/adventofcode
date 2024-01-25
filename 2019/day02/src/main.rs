const INPUT: &str = include_str!("input");

fn main() {
   let mut program: Vec<usize> = INPUT
       .trim()
       .split(",")
       .map(|s| s.parse().unwrap())
       .collect();

   program[1] = 12;
   program[2] = 2;

   let mut pos = 0;

   while program[pos] != 99 {
      let opcode = program[pos];
      let in1 = program[pos + 1];
      let in2 = program[pos + 2];
      let out = program[pos + 3];

      if opcode == 1 {
         program[out] = program[in1] + program[in2];
      } else {
         program[out] = program[in1] * program[in2];
      }

      pos += 4;
   }

   println!("Part 1: {}", program[0]); // 10566835
}

