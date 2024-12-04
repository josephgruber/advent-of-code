use anyhow::Result;
use aoc_03::solutions;
use code_timing_macros::time_snippet;
use std::fs;

fn main() -> Result<()> {
    let input = fs::read_to_string("input/input.txt")?;

    let part1_result = time_snippet!(solutions::part1(&input)?);
    println!("Part 1 Result: {:.2}", part1_result);

    println!("---");

    let part2_result = time_snippet!(solutions::part2(&input)?);
    println!("Part 2 Result: {:.2}", part2_result);

    Ok(())
}
