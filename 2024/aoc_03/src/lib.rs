use anyhow::Result;
use regex::Regex;

pub mod solutions {
    use super::*;

    pub fn part1(input: &str) -> Result<usize> {
        let pattern = Regex::new(r"mul\((?<x>\d{1, 3}),(?<y>\d{1, 3})\)").unwrap();

        Ok(pattern
            .captures_iter(input)
            .map(|capture| {
                capture["x"].parse::<usize>().unwrap() * capture["y"].parse::<usize>().unwrap()
            })
            .sum())
    }

    pub fn part2(input: &str) -> Result<i32> {
        let mut enabled: bool = true;
        let mut result: i32 = 0;
        let pattern = Regex::new(r"(mul\((?<x>\d{1,3}),(?<y>\d{1,3})\)|don't\(\)|do\(\))").unwrap();

        for capture in pattern.captures_iter(input) {
            match capture[0].as_ref() {
                "do()" => enabled = true,
                "don't()" => enabled = false,
                _ if enabled => {
                    result +=
                        capture["x"].parse::<i32>().unwrap() * capture["y"].parse::<i32>().unwrap();
                }
                _ => (),
            }
        }

        Ok(result)
    }
}
