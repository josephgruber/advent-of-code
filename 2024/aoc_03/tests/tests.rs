use aoc_03::solutions;

const TEST_STR_PART_1: &str =
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
const TEST_STR_PART_2: &str =
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR_PART_1);
    assert_eq!(result.unwrap(), 161);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR_PART_2);
    assert_eq!(result.unwrap(), 48);
}
