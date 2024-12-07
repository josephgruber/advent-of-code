use anyhow::Result;

#[derive(Debug)]
struct Equation {
    result: usize,
    values: Vec<usize>,
}

fn parse_equations(input: &str) -> Result<Vec<Equation>> {
    let mut equations = Vec::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split(':').collect();
        let result = parts[0].trim().parse::<usize>()?;
        let values: Result<Vec<usize>, _> = parts[1]
            .split_whitespace()
            .map(|n| n.parse::<usize>())
            .collect();

        equations.push(Equation {
            result,
            values: values?,
        });
    }

    Ok(equations)
}

fn concatenate(a: usize, b: usize) -> usize {
    format!("{}{}", a, b).parse().unwrap()
}

fn is_valid(equation: &Equation, enable_concatenate: bool) -> bool {
    let mut possible_results = vec![equation.values[0]];

    for &value in equation.values.iter().skip(1) {
        let mut new_results = Vec::new();
        for &current in &possible_results {
            let sum = current + value;
            if sum == equation.result {
                return true;
            }
            new_results.push(sum);

            let product = current * value;
            if product == equation.result {
                return true;
            }
            new_results.push(product);

            if enable_concatenate {
                let concat = concatenate(current, value);
                if concat == equation.result {
                    return true;
                }
                new_results.push(concat);
            }
        }
        possible_results = new_results;
    }

    false
}

pub mod solutions {
    use super::*;

    pub fn part1(input: &str) -> Result<usize> {
        let equations = parse_equations(input)?;
        let result = equations
            .iter()
            .filter(|equation| is_valid(equation, false))
            .map(|equation| equation.result)
            .sum();

        Ok(result)
    }

    pub fn part2(input: &str) -> Result<usize> {
        let equations = parse_equations(input)?;
        let result = equations
            .iter()
            .filter(|equation| is_valid(equation, true))
            .map(|equation| equation.result)
            .sum();

        Ok(result)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

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
    fn test_parse_equations() {
        let equations = parse_equations(TEST_STR).unwrap();
        assert_eq!(equations.len(), 9);
        assert_eq!(equations[0].result, 190);
        assert_eq!(equations[0].values, vec![10, 19]);
        assert_eq!(equations[8].result, 292);
        assert_eq!(equations[8].values, vec![11, 6, 16, 20]);
    }

    #[test]
    fn test_is_valid_without_concatenation() {
        let enable_concatenate = false;
        let equations = parse_equations(TEST_STR).unwrap();

        assert!(is_valid(&equations[0], enable_concatenate));
        assert!(is_valid(&equations[1], enable_concatenate));
        assert!(!is_valid(&equations[2], enable_concatenate));
        assert!(!is_valid(&equations[3], enable_concatenate));
        assert!(!is_valid(&equations[4], enable_concatenate));
        assert!(!is_valid(&equations[5], enable_concatenate));
        assert!(!is_valid(&equations[6], enable_concatenate));
        assert!(!is_valid(&equations[7], enable_concatenate));
        assert!(is_valid(&equations[8], enable_concatenate));
    }

    #[test]
    fn test_is_valid_with_concatenation() {
        let enable_concatenate = true;
        let equations = parse_equations(TEST_STR).unwrap();

        assert!(is_valid(&equations[0], enable_concatenate));
        assert!(is_valid(&equations[1], enable_concatenate));
        assert!(!is_valid(&equations[2], enable_concatenate));
        assert!(is_valid(&equations[3], enable_concatenate));
        assert!(is_valid(&equations[4], enable_concatenate));
        assert!(!is_valid(&equations[5], enable_concatenate));
        assert!(is_valid(&equations[6], enable_concatenate));
        assert!(!is_valid(&equations[7], enable_concatenate));
        assert!(is_valid(&equations[8], enable_concatenate));
    }
}
