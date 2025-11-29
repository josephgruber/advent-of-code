use anyhow::Result;

struct Guard {
    direction: u8,
    position: Point,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }
}

struct Grid {
    cells: Vec<u8>,
    width: usize,
    height: usize,
}

impl Grid {
    fn new(width: usize, height: usize) -> Self {
        Grid {
            cells: vec![0; width * height],
            width,
            height,
        }
    }

    fn get(&self, point: Point) -> Option<u8> {
        // Handle negative coordinates and conversion to usize
        if point.x < 0 || point.y < 0 {
            return None;
        }
        let x = point.x as usize;
        let y = point.y as usize;

        if x < self.width && y < self.height {
            Some(self.cells[y * self.width + x])
        } else {
            None
        }
    }

    fn set(&mut self, point: Point, value: u8) -> bool {
        // Handle negative coordinates and conversion to usize
        if point.x < 0 || point.y < 0 {
            return false;
        }
        let x = point.x as usize;
        let y = point.y as usize;

        if x < self.width && y < self.height {
            self.cells[y * self.width + x] = value;
            true
        } else {
            false
        }
    }

    fn find_guard(&self) -> Option<Point> {
        const GUARD_CHAR: u8 = b'^';

        for y in 0..self.height {
            for x in 0..self.width {
                if self.cells[y * self.width + x] == GUARD_CHAR {
                    return Some(Point::new(x as i32, y as i32));
                }
            }
        }
        None
    }

    fn in_bounds(&self, point: Point) -> bool {
        point.x >= 0
            && point.y >= 0
            && (point.x as usize) < self.width
            && (point.y as usize) < self.height
    }

    fn iter(&self) -> impl Iterator<Item = (Point, u8)> + '_ {
        (0..self.height).flat_map(move |y| {
            (0..self.width).map(move |x| {
                (
                    Point::new(x as i32, y as i32),
                    self.cells[y * self.width + x],
                )
            })
        })
    }
}

fn parse_grid(input: &str) -> (Vec<Vec<u8>>, Guard) {
    let mut guard = None;

    let lines: Vec<_> = input.lines().collect();
    let height = lines.len();
    let width = lines.get(0).map_or(0, |line| line.len());

    let mut grid = Vec::with_capacity(height);

    for (y, line) in lines.into_iter().enumerate() {
        let mut row = Vec::with_capacity(width);
        for (x, b) in line.bytes().enumerate() {
            if b == GUARD_CHAR {
                guard = Some(Guard {
                    direction: b,
                    position: Point::new(x as i32, y as i32),
                });
                row.push(b'.');
            } else {
                row.push(b);
            }
        }
        grid.push(row);
    }

    guard.map_or(Err("No guard found"), |g| Ok((grid, g)))
}

pub mod solutions {
    use super::*;

    pub fn part1(input: &str) -> Result<usize> {
        Ok(1)
    }

    pub fn part2(input: &str) -> Result<usize> {
        Ok(2)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_STR: &str = "";
}
