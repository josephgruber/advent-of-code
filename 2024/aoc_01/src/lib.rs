use itertools::Itertools;

fn split_list(input: &str) -> (Vec<u32>, Vec<u32>) {
    // Converts the string of integers into a list of left integer and right integers
    input
        .lines()
        .map(|line| {
            let mut numbers = line.split_whitespace().map(|n| n.parse::<u32>().unwrap());
            (numbers.next().unwrap(), numbers.next().unwrap())
        })
        .unzip()
}

fn calc_distances(left_numbers: &[u32], right_numbers: &[u32]) -> Vec<u32> {
    // Determines the absolute difference between the left and right integers
    left_numbers
        .iter()
        .sorted()
        .zip(right_numbers.iter().sorted())
        .map(|(left, right)| left.abs_diff(*right))
        .collect()
}

fn calc_similarities(left_numbers: &[u32], right_numbers: &[u32]) -> Vec<u32> {
    // Determines the similarities between the left and right integers
    left_numbers
        .iter()
        .map(|left_number| {
            right_numbers
                .iter()
                .filter(|&right_number| right_number == left_number)
                .count() as u32
                * left_number
        })
        .collect()
}

pub mod solutions {
    pub fn part1(input: &str) -> u32 {
        let (left_numbers, right_numbers) = super::split_list(input);
        let distances = super::calc_distances(&left_numbers, &right_numbers);
        distances.iter().sum()
    }

    pub fn part2(input: &str) -> u32 {
        let (left_numbers, right_numbers) = super::split_list(input);
        let similarities = super::calc_similarities(&left_numbers, &right_numbers);
        similarities.iter().sum()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

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
}
