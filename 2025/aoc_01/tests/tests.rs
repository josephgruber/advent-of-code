use aoc_01::solutions;

const TEST_STR: &str = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

#[test]
fn test_part1() {
    let result = solutions::part1(TEST_STR);
    assert_eq!(result.unwrap(), 3);
}

#[test]
fn test_part2() {
    let result = solutions::part2(TEST_STR);
    assert_eq!(result.unwrap(), 6);
}
