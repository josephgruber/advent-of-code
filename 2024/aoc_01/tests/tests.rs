use aoc_01::solutions;

const TEST_STR: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR);
    assert_eq!(result, 11);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR);
    assert_eq!(result, 31);
}
