use aoc_06::solutions;

const TEST_STR: &str = "";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR);
    assert_eq!(result.unwrap(), 1);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR);
    assert_eq!(result.unwrap(), 2);
}
