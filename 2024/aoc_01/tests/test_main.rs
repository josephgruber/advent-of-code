use aoc_01::{calc_distances, calc_similarities, solutions, split_list};

const TEST_STR: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

#[test]
fn test_split_list() {
    let (left, right) = split_list(TEST_STR);
    assert_eq!(left, vec![3, 4, 2, 1, 3, 3]);
    assert_eq!(right, vec![4, 3, 5, 3, 9, 3]);
}

#[test]
fn test_calc_distances() {
    let (left_numbers, right_numbers) = split_list(TEST_STR);
    let distances = calc_distances(&left_numbers, &right_numbers);
    assert_eq!(distances, vec![2, 1, 0, 1, 2, 5]);
}

#[test]
fn test_calc_similarities() {
    let (left_numbers, right_numbers) = split_list(TEST_STR);
    let similarities = calc_similarities(&left_numbers, &right_numbers);
    assert_eq!(similarities, vec![9, 4, 0, 0, 9, 9]);
}

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
