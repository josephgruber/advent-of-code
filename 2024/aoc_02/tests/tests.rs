use aoc_02::solutions;

const TEST_STR: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR);
    assert_eq!(result.unwrap(), 2);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR);
    assert_eq!(result.unwrap(), 4);
}
