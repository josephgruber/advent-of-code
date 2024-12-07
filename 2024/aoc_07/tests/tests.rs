use aoc_07::solutions;

const TEST_STR: &str = "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR);
    assert_eq!(result.unwrap(), 3749);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR);
    assert_eq!(result.unwrap(), 11387);
}
