const INPUT: &str = include_str!("input");

fn main() {
   let mut program: Vec<usize> = INPUT
       .trim()
       .split(",")
       .map(|s| s.parse().unwrap())
       .collect();

   program[1] = 12;
   program[2] = 2;

   let part1 = run_program(program.clone());

   println!("Part 1: {}", part1[0]); // 10566835

   for a in 0..50 {
      for b in 0..50 {
         program[1] = a;
         program[2] = b;

         let part2 = run_program(program.clone());

         if part2[0] == 19690720 {
            println!("Part 2: a = {}, b = {}, answer = {}", a, b, 100 * a + b); // 2347
         }
      }
   }
}

fn run_program(mut program: Vec<usize>) -> Vec<usize> {
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

   program
}