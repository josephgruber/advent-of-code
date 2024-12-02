use aoc_01::solutions;
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn criterion_benchmark(c: &mut Criterion) {
    let input = include_str!("../input/input.txt");

    c.bench_function("solutions::part1", |b| {
        b.iter(|| solutions::part1(black_box(input)))
    });

    c.bench_function("solutions::part2", |b| {
        b.iter(|| solutions::part2(black_box(input)))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
