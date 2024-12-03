use anyhow::Result;

fn parse_reports(input: &str) -> impl Iterator<Item = Vec<usize>> + '_ {
    // Parses the input text and returns an iterator that contains
    // each row (report) and it's individual levels (integers)
    input.lines().map(|line| {
        line.split_whitespace()
            .map(|num| num.parse::<usize>().unwrap())
            .collect()
    })
}

fn is_safe(report: &[usize]) -> bool {
    // Determines if the report (row from input) is either continuously ascending or descending
    // along with verifying the absolute difference between each value is between 1 and 3
    let is_ascending = report.is_sorted_by(|a, b| a < b && (1..=3).contains(&a.abs_diff(*b)));
    let is_descending = report.is_sorted_by(|a, b| a > b && (1..=3).contains(&a.abs_diff(*b)));

    is_ascending || is_descending
}

fn is_safe_with_problem_dampener(report: &[usize]) -> bool {
    // Adds the Problem Dampener. First checks if the entire report (row) is safe, and
    // if not, creates slices of each row removing a single level (index) for each slice
    // before testing if that report slice is safe
    if is_safe(report) {
        return true;
    }

    for level in 0..report.len() {
        if is_safe(
            &report
                .iter()
                .enumerate()
                .filter(|&(idx, _)| idx != level)
                .map(|(_, &val)| val)
                .collect::<Vec<_>>(),
        ) {
            return true;
        }
    }

    false
}

pub mod solutions {
    use super::*;

    pub fn part1(input: &str) -> Result<usize> {
        let reports = parse_reports(input);

        Ok(reports
            .collect::<Vec<_>>()
            .iter()
            .filter(|report| is_safe(report))
            .count())
    }

    pub fn part2(input: &str) -> Result<usize> {
        let reports = parse_reports(input);

        Ok(reports
            .collect::<Vec<_>>()
            .iter()
            .filter(|report| is_safe_with_problem_dampener(report))
            .count())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_STR: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

    #[test]
    fn test_parse_reports() {
        let reports: Vec<Vec<usize>> = parse_reports(TEST_STR).collect();
        assert_eq!(reports.len(), 6);
        assert_eq!(reports[0], vec![7, 6, 4, 2, 1]);
        assert_eq!(reports[1], vec![1, 2, 7, 8, 9]);
        assert_eq!(reports[2], vec![9, 7, 6, 2, 1]);
        assert_eq!(reports[3], vec![1, 3, 2, 4, 5]);
        assert_eq!(reports[4], vec![8, 6, 4, 4, 1]);
        assert_eq!(reports[5], vec![1, 3, 6, 7, 9]);
    }

    #[test]
    fn test_is_safe() {
        let reports: Vec<Vec<usize>> = parse_reports(TEST_STR).collect();
        assert!(is_safe(&reports[0]));
        assert!(!is_safe(&reports[1]));
        assert!(!is_safe(&reports[2]));
        assert!(!is_safe(&reports[3]));
        assert!(!is_safe(&reports[4]));
        assert!(is_safe(&reports[5]));
    }

    #[test]
    fn test_is_safe_with_problem_dampener() {
        let reports: Vec<Vec<usize>> = parse_reports(TEST_STR).collect();
        assert!(is_safe_with_problem_dampener(&reports[0]));
        assert!(!is_safe_with_problem_dampener(&reports[1]));
        assert!(!is_safe_with_problem_dampener(&reports[2]));
        assert!(is_safe_with_problem_dampener(&reports[3]));
        assert!(is_safe_with_problem_dampener(&reports[4]));
        assert!(is_safe_with_problem_dampener(&reports[5]));
    }
}
