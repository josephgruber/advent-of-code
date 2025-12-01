use anyhow::Result;
// use aoc_common::*;

pub mod solutions {
    use super::*;

    pub fn part1(input: &str) -> Result<usize> {
        let mut position = 50;
        let mut zero_count = 0;

        for line in input.lines() {
            let direction = line.chars().next().unwrap();
            let distance = line[1..].parse::<u32>().unwrap();

            match direction {
                'R' => position = (position + distance) % 100,
                'L' => position = (position + 100 - (distance % 100)) % 100,
                _ => {}
            }

            if position == 0 {
                zero_count += 1;
            }
        }

        Ok(zero_count)
    }

    pub fn part2(input: &str) -> Result<usize> {
        let mut position = 50;
        let mut zero_count: usize = 0;

        for line in input.lines() {
            let direction = line.chars().next().unwrap();
            let distance = line[1..].parse::<u32>().unwrap();

            match direction {
                'R' => {
                    let first_zero = (100 - position) % 100;
                    if first_zero != 0 && first_zero <= distance {
                        zero_count += (1 + (distance - first_zero) / 100) as usize;
                    }
                    position = (position + distance) % 100;
                }
                'L' => {
                    if position != 0 && position <= distance {
                        zero_count += (1 + (distance - position) / 100) as usize;
                    }
                    position = (position + 100 - (distance % 100)) % 100;
                }
                _ => {}
            }
        }

        Ok(zero_count)
    }
}
