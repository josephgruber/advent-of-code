use itertools::Itertools;

pub fn split_list(input: &str) -> (Vec<u32>, Vec<u32>) {
    // Converts the string of integers into a list of left integer and right integers
    input
        .lines()
        .map(|line| {
            let mut numbers = line.split_whitespace().map(|n| n.parse::<u32>().unwrap());
            (numbers.next().unwrap(), numbers.next().unwrap())
        })
        .unzip()
}

pub fn calc_distances(left_numbers: &[u32], right_numbers: &[u32]) -> Vec<u32> {
    // Determines the absolute difference between the left and right integers
    left_numbers
        .iter()
        .sorted()
        .zip(right_numbers.iter().sorted())
        .map(|(left, right)| left.abs_diff(*right))
        .collect()
}

pub fn calc_similarities(left_numbers: &[u32], right_numbers: &[u32]) -> Vec<u32> {
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
    use timing_macro::measure_time;

    #[measure_time]
    pub fn part1(input: &str) -> u32 {
        let (left_numbers, right_numbers) = super::split_list(input);
        let distances = super::calc_distances(&left_numbers, &right_numbers);
        distances.iter().sum()
    }

    #[measure_time]
    pub fn part2(input: &str) -> u32 {
        let (left_numbers, right_numbers) = super::split_list(input);
        let similarities = super::calc_similarities(&left_numbers, &right_numbers);
        similarities.iter().sum()
    }
}
